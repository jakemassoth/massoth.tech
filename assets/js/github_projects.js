function getGithubProjects(url, username, cb) {
    "use strict";

    var xhttp = new XMLHttpRequest();
    var reqURL = url + `?username=${username}`;
    reqURL = reqURL.split(" ").join("");

    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          cb(this);
        }
     };
      xhttp.open("GET", reqURL, true);
      xhttp.send();
}

function insertProjectsHTML(xhttp) {
    "use strict";

    var projectsJSON = JSON.parse(xhttp.responseText);

    // sort by most recently commited to on Github
    projectsJSON = projectsJSON.sort((function (a, b) {
        return new Date(b.node.pushedAt) - new Date(a.node.pushedAt); 
    }));

    var projectDivs = [];

    projectsJSON.forEach((item) => {
        // Pretty-print the UTC timestamp
        item = item.node;
        var date = new Date(item.pushedAt);
        var dateString = date.toDateString();

        var html = `<div class="col-lg-4 col-sm-6 portfolio-item">
                        <div class="card h-100">
                            <div class="card-body">
                                <h5 class="card-title">
                                    <a target="_blank" href="${item.url}">${item.name}</a>
                                </h5>
                                <h6 class="card-subtitle mb-2 text-muted">${item.primaryLanguage !== null ? item.primaryLanguage.name : ''}
                                </h6>
                                <p class="card-text"> ${ item.description !== null ? item.description : '' } </p>
                            </div>
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item">
                                    <i class="fas fa-star"></i>: ${item.stargazerCount}
                                </li>
                                <li class="list-group-item">
                                    <i class="fas fa-code-branch"></i>: ${item.forkCount}
                                </li>
                                <li class="list-group-item">
                                    Last Commit: ${dateString}
                                </li>
                            </ul>
                        </div>
                    </div>`;
        
        projectDivs.push(html);
    });


    document.getElementById("github-projects").innerHTML = projectDivs.join("\n");
}