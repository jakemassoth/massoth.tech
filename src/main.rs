use std::fs;

use maud::{DOCTYPE, Markup, html};

fn base_layout(title: &str, content: Markup) -> Markup {
    html! {
    (DOCTYPE)
    head {
        meta charset="utf-8" {}
        link rel="icon" type="image/svg+xml" href="/public/favicon.svg" {}
        link rel="stylesheet" type="text/css" href="/public/main.css"
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
            }
            content {
                (content)

            }
        }
    }
}

fn index_page() -> Markup {
    let index_content = html! {
        section {
            h1 {("Hi, I'm Jake.")}
        }
    };

    base_layout("Home", index_content)
}
fn main() -> Result<(), std::io::Error> {
    if fs::exists("./dist").unwrap_or_default() {
        fs::remove_dir_all("./dist")?;
    }
    fs::create_dir_all("./dist/public")?;
    fs::copy("./public/main.css", "./dist/public/main.css")?;
    fs::copy("./public/favicon.svg", "./dist/public/favicon.ico")?;

    fs::write("./dist/index.html", index_page().into_string())?;
    Ok(())
}
