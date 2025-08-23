use std::{ffi::OsStr, fs};

use comrak::{Options, markdown_to_html};
use gray_matter::{Matter, engine::YAML};
use maud::{DOCTYPE, Markup, PreEscaped, html};
use serde::Deserialize;

fn base_layout(title: &str, content: Markup) -> Markup {
    html! {
        (DOCTYPE)
        head {
            meta charset="utf-8" {}
            link rel="icon" type="image/svg+xml" href="/public/favicon.svg" {}
            link rel="stylesheet" type="text/css" href="/public/main.css" {}
            meta name="viewport" content="width=device-width, initial-scale=1.0" {}
            title { (title) }
        }

        body {
            main {
                div class="nav" {
                    a href="/" {( "Home" )}
                    a href="/blog" {("Blog")}
                    a href="/about" {("About")}
                }
                content {
                    (content)
                }
            }
        }
    }
}

fn index_page(project_entries: Vec<Markup>) -> Markup {
    let index_content = html! {
        section {
            h1 {("Hi, I'm Jake.")}
            section class="links" {
                a class="styled-link" href="https://github.com/jakemassoth" {("Github")}
                a class="styled-link" href="https://www.linkedin.com/in/jakemassoth/" {("LinkedIn")}
            }
            p {
                ("I'm a full stack engineer with a product mindset and an eye for developer experience.")
            }
            p {
                ("On this site you can check out my blog, read about some of my projects, or read more about me.")
            }
        }
        section {
            h2 {("Projects")}
            div class="projects" {
                @for project in &project_entries {
                    (project)
                }
            }
        }
    };

    base_layout("Home", index_content)
}

#[derive(Deserialize, Debug)]
struct ProjectFrontMatter {
    article: Option<String>,
    repo: Option<String>,
    year: i32,
    title: String,
}

struct ProjectEntry {
    body: String,
    data: ProjectFrontMatter,
}

impl ProjectEntry {
    fn new(markdown_content: String) -> Option<ProjectEntry> {
        let matter = Matter::<YAML>::new();
        let front_matter = matter.parse::<ProjectFrontMatter>(&markdown_content).ok()?;
        let mut options = Options::default();
        options.extension.front_matter_delimiter = Some("---".to_owned());
        let markdown_body = markdown_to_html(&markdown_content, &options);

        let front_matter_data = front_matter.data?;
        Some(ProjectEntry {
            data: front_matter_data,
            body: markdown_body,
        })
    }
    fn to_markup(&self) -> Markup {
        html! {
            div class="project" {
                div class="project-front" {
                    h3 {(self.data.title)}
                    div class="project-body" {(PreEscaped(self.body.clone()))}
                    div class="project-links" {
                        @if let Some(link) = &self.data.article {
                            a class="styled-link" href=(link) {("Article")}
                        } @else if let Some(link) = &self.data.repo {
                            a class="styled-link" href=(link) {("Repo")}
                        } @else { ("") }
                    }
                }
            }
        }
    }
}

fn setup_dist_dir() -> Result<(), std::io::Error> {
    if fs::exists("./dist").unwrap_or_default() {
        fs::remove_dir_all("./dist")?;
    }
    fs::create_dir_all("./dist/public")?;
    fs::copy("./public/main.css", "./dist/public/main.css")?;
    fs::copy("./public/favicon.svg", "./dist/public/favicon.svg")?;
    Ok(())
}

fn get_projects() -> Result<Vec<ProjectEntry>, std::io::Error> {
    let mut entries_sorted = fs::read_dir("./content/projects")
        .map_err(|e| {
            eprintln!(
                "Failed to read projects directory: {}. make sure ./content/projects exists.",
                e
            );
            e
        })?
        .filter_map(|entry| {
            let e = entry.ok()?;
            let path = e.path();
            println!("{}", path.display());

            if path.extension() == Some(OsStr::new("md")) {
                fs::read_to_string(path).ok()
            } else {
                eprintln!("failed to read path {}", path.display());
                None
            }
        })
        .filter_map(|markdown_content| ProjectEntry::new(markdown_content))
        .collect::<Vec<ProjectEntry>>();

    entries_sorted.sort_by_key(|entry| entry.data.year);
    entries_sorted.reverse();
    Ok(entries_sorted)
}

fn main() -> Result<(), std::io::Error> {
    setup_dist_dir()?;

    let projects_markup = get_projects()?
        .into_iter()
        .map(|entry| entry.to_markup())
        .collect::<Vec<Markup>>();

    fs::write(
        "./dist/index.html",
        index_page(projects_markup).into_string(),
    )?;

    Ok(())
}
