import fs from "fs";
import express from "exp";

const htmlHit = fs.readFileSync("./data.html", {
  encoding: "utf-8",
  flag: "r",
});
const htmlMiss = fs.readFileSync("./nodata.html", {
  encoding: "utf-8",
  flag: "r",
});

const app = express();

app.post("/", (req, res) => {});

// const http = require("http");

const htmlResponseHit = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PCNS</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i&display=swap" rel="stylesheet">
    <link href="/Content/Site.css" rel="stylesheet"/>

    <link href="/Content/bootstrap.css" rel="stylesheet"/>
<link href="/Content/site.css" rel="stylesheet"/>

    <script src="/Scripts/modernizr-2.8.3.js"></script>


</head>

<!--Use the below code snippet to provide real time updates to the live chat plugin without the need of copying and paste each time to your website when changes are made via PBX-->
<call-us-selector phonesystem-url="https://boardofhealthcarefunders.3cx.sc:5001" party="LiveChat124091"></call-us-selector>
<script defer src="https://downloads-global.3cx.com/downloads/livechatandtalk/v1/callus.js" id="tcx-callus-js" charset="utf-8"></script>

<body>

    
    <div style="font-size: 18px; color: white; background-color: #801424; text-align: center ; padding-top: 5px;">
        IMPORTANT NOTICE: WEBCHAT Unavailable. Click <a style="color: white !important; font-weight: 600 !important;" href="/documents/PCNS_IMPORTANT_NOTICE.pdf">here</a>.
    </div>
    
    

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <div class="container">
            <a class="navbar-brand" href="/"></a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavDropdown">
                <ul class="navbar-nav">
                    <li class="nav-item active">

                        <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/Home/News">News</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Information
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                            <a class="dropdown-item" href="/Home/Fees" target="">Fees</a>
                            
                            <a class="dropdown-item" href="/Home/WhatsNew" target="">What&#39;s New</a>
                            <a class="dropdown-item" href="/Home/FundingOrganisations" target="">How to for Funders</a>
                            <a class="dropdown-item" href="/Home/HealthcareServiceProviders" target="">How to for Healthcare Service Providers</a>

                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            PCNS Forms
                        </a>
                        <div class="dropdown-menu">
                            <a class="dropdown-item" href="/ApplicationForms" target="">Application Forms</a>
                            <a class="dropdown-item" href="/ApplicationForms/UpdateForms" target="">Update Forms</a>
                        </div>
                    </li>
                    <li> <a class="nav-link" href="/Payment/CheckBalance">Payment</a></li>
                    <li><a class="nav-link" href="/Search/Verify">Verify Practice</a></li>

                </ul>
                
<ul class="navbar-nav ml-auto">

    

    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" aria-expanded="false">Funding Organisations<span class="caret"></span></a>
        <ul class="dropdown-menu">
            <li>
                <a class="dropdown-item" href="/Account/Login" id="registerLink">Login</a>
            </li>
            <li>
                <a class="dropdown-item" href="/Account/RegisterOrganisation" id="registerLink">Register</a>
            </li>
        </ul>
    </li>

    <li class="dropdown">
        <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" aria-expanded="false">Healthcare Service Providers<span class="caret"></span></a>
        <ul class="dropdown-menu">
            
            <li>
                <a class="dropdown-item" href="/Account/RegisterHealthcare" id="registerLink">Register</a>
            </li>
        </ul>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="https://www.bhfportal.co.za/bhfglobal/" target="_blank">Analytics</a>
    </li>
    

</ul>

            </div>
        </div>
    </nav>


    

    <div class="">
        
        



<div class="container body-content">

    <h2>Verify Practice Number</h2>

    <br />
<form action="/Search/Verify" class="form-horizontal" method="post" role="form"><input name="__RequestVerificationToken" type="hidden" value="J6o4u8t63ICme8XazSyjeNgdRyTQO6zXWbINqhV5id-zKVwzpul-1QN9-iW6iKv3A4wOSHk2K0EIF6P9hOSo7NKgOu5KABAlVawAOBOAo3Y1" />        <div>
            <div>
                <h5>Practice Number:</h5>
                <input class="form-control" id="SearchValue" name="SearchValue" type="text" value="1429124" /> <br />
                <input type="submit" class="btn btn-primary" value="Verify" />
            </div>
        </div>
        <br />
        <br />
            <table class="table">
                <tr>
                    <th>Practice Number</th>
                    <th>Name</th>
                    <th>Date Registered</th>
                    <th>Status</th>
                    <th>Dispensing License</th>
                </tr>
                <tr>
                    <td>1429124</td>
                    <td>Dr JOHAN OLIVIER</td>
                    <td>01-07-1991  </td>
                    <td>ACTIVE </td>
                    <td>No </td>
                </tr>
            </table>
</form>
</div>



        <hr />
        <footer style="text-align: center">
            <p>&copy; 2024 - BHF</p>
        </footer>
    </div>

    <script src="/Scripts/jquery-3.4.1.js"></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
    
    <script src="/Scripts/jquery.validate.js"></script>
<script src="/Scripts/jquery.validate.unobtrusive.js"></script>

    
</body>
</html>
`;

const htmlResponseMiss = `

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PCNS</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i&display=swap" rel="stylesheet">
    <link href="/Content/Site.css" rel="stylesheet"/>

    <link href="/Content/bootstrap.css" rel="stylesheet"/>
<link href="/Content/site.css" rel="stylesheet"/>

    <script src="/Scripts/modernizr-2.8.3.js"></script>


</head>

<!--Use the below code snippet to provide real time updates to the live chat plugin without the need of copying and paste each time to your website when changes are made via PBX-->
<call-us-selector phonesystem-url="https://boardofhealthcarefunders.3cx.sc:5001" party="LiveChat124091"></call-us-selector>
<script defer src="https://downloads-global.3cx.com/downloads/livechatandtalk/v1/callus.js" id="tcx-callus-js" charset="utf-8"></script>

<body>

    
    <div style="font-size: 18px; color: white; background-color: #801424; text-align: center ; padding-top: 5px;">
        IMPORTANT NOTICE: WEBCHAT Unavailable. Click <a style="color: white !important; font-weight: 600 !important;" href="/documents/PCNS_IMPORTANT_NOTICE.pdf">here</a>.
    </div>
    
    

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <div class="container">
            <a class="navbar-brand" href="/"></a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavDropdown">
                <ul class="navbar-nav">
                    <li class="nav-item active">

                        <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/Home/News">News</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Information
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                            <a class="dropdown-item" href="/Home/Fees" target="">Fees</a>
                            
                            <a class="dropdown-item" href="/Home/WhatsNew" target="">What&#39;s New</a>
                            <a class="dropdown-item" href="/Home/FundingOrganisations" target="">How to for Funders</a>
                            <a class="dropdown-item" href="/Home/HealthcareServiceProviders" target="">How to for Healthcare Service Providers</a>

                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            PCNS Forms
                        </a>
                        <div class="dropdown-menu">
                            <a class="dropdown-item" href="/ApplicationForms" target="">Application Forms</a>
                            <a class="dropdown-item" href="/ApplicationForms/UpdateForms" target="">Update Forms</a>
                        </div>
                    </li>
                    <li> <a class="nav-link" href="/Payment/CheckBalance">Payment</a></li>
                    <li><a class="nav-link" href="/Search/Verify">Verify Practice</a></li>

                </ul>
                
<ul class="navbar-nav ml-auto">

    

    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" aria-expanded="false">Funding Organisations<span class="caret"></span></a>
        <ul class="dropdown-menu">
            <li>
                <a class="dropdown-item" href="/Account/Login" id="registerLink">Login</a>
            </li>
            <li>
                <a class="dropdown-item" href="/Account/RegisterOrganisation" id="registerLink">Register</a>
            </li>
        </ul>
    </li>

    <li class="dropdown">
        <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" aria-expanded="false">Healthcare Service Providers<span class="caret"></span></a>
        <ul class="dropdown-menu">
            
            <li>
                <a class="dropdown-item" href="/Account/RegisterHealthcare" id="registerLink">Register</a>
            </li>
        </ul>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="https://www.bhfportal.co.za/bhfglobal/" target="_blank">Analytics</a>
    </li>
    

</ul>

            </div>
        </div>
    </nav>


    

    <div class="">
        
        


<div class="container body-content">

    <h1 class="text-info">Oops!</h1>
    <hr />

    <h2 class="text-info">Could not find Practice Number 12.</h2>

</div>
        <hr />
        <footer style="text-align: center">
            <p>&copy; 2024 - BHF</p>
        </footer>
    </div>

    <script src="/Scripts/jquery-3.4.1.js"></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
    

    
</body>
</html>
`;

const server = http.createServer((req, res) => {
  // Set status code and headers
  res.writeHead(200, { "Content-Type": "text/html" });

  // Wait for 5 seconds before responding
  setTimeout(() => {
    // Send response after 5 seconds
    res.end(htmlResponseHit);
  }, 5000); // 5000 milliseconds = 5 seconds
});

const PORT = 3000; // Choose any port you want
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
