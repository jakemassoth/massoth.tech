function getGithubProjects(username, cb) {
    "use strict";
    var xhttp = new XMLHttpRequest();
    var url = `https://api.github.com/users/${username}/repos`;

    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          cb(this);
        }
     };
      xhttp.open("GET", url, true);
      xhttp.send();
}

function insertProjectsHTML(xhttp) {
    "use strict";
    var projectsJSON = JSON.parse(xhttp.responseText);

    // sort by most recently commited to on Github
    projectsJSON = projectsJSON.sort((function (a, b) {
        return new Date(b.updated_at) - new Date(a.updated_at); 
    }));

    var projectDivs = [];

    Object.keys(projectsJSON).forEach(function(key) {
        var html = `<div class="col-lg-4 col-sm-6 portfolio-item">
                        <div class="card h-100">
                            <div class="card-body">
                                <h5 class="card-title">
                                    <a target="_blank" href="${projectsJSON[key].html_url}">${projectsJSON[key].name}</a>
                                </h5>
                                <h6 class="card-subtitle mb-2 text-muted">${projectsJSON[key].language !== null ? projectsJSON[key].language : ''}
                                </h6>
                                <p class="card-text"> ${ projectsJSON[key].description !== null ? projectsJSON[key].description : '' } </p>
                            </div>
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item">
                                    <i class="fas fa-star"></i>: ${projectsJSON[key].stargazers_count}
                                </li>
                                <li class="list-group-item">
                                    <i class="fas fa-code-branch"></i>: ${projectsJSON[key].forks_count}
                                </li>
                                <li class="list-group-item">
                                    Most Recent Commit: ${projectsJSON[key].updated_at}
                                </li>
                            </ul>
                        </div>
                    </div>`;
        
        projectDivs.push(html);

    });


    document.getElementById("github-projects").innerHTML = projectDivs.join("\n");
}