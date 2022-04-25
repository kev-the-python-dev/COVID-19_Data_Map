<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url] 
[![Forks][forks-shield]][forks-url] 
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kevin-douglas/covid19project-backend">
    <img src="https://i.imgur.com/erOoYPp.png" alt="Logo" height="80">
  </a>

<h3 align="center">COVID-19 Interactive Data Map (U.S.)</h3>

  <p align="center">
    An interactive map made with primarily made with Django, Python, & Javascript that uses data from https://github.com/CSSEGISandData/COVID-19 to display the most recent reported data regarding COVID-19 infections. 
    <br />
    <a href="https://github.com/kevin-douglas/covid19project-backend"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kevin-douglas/covid19project-backend/blob/main/mymap/static/geocovdata.json">View Demo</a>
    ·
    <a href="https://github.com/kevin-douglas/covid19project-backend/issues">Report Bug</a>
    ·
    <a href="https://github.com/kevin-douglas/covid19project-backend/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src='https://raw.githubusercontent.com/kevin-douglas/covid19project-backend/main/map_marker_data_view.png'>

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)
* [Django](https://www.djangoproject.com/)
* [JQuery](https://jquery.com)
* [Leaflet](https://leafletjs.com/)
* [MapBox](https://www.mapbox.com/)
* [SQLite3](https://sqlite.org/index.html)
* [SpatialLite](https://www.gaia-gis.it/fossil/libspatialite/index)
* [PROJ](https://proj.org/)
* [GEOS](https://trac.osgeo.org/geos/)
* [GDAL](https://gdal.org/)
<br>

Personally, I used Fedora 35 as my distro and thus some of the required libraries _required_ a different process to get GeoDjango, Spatialite, PROJ, GEOS, and GDAL implemented correctly. I'll drop the sources here once compiled in an organized fashion. 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
  pip install -r requirements.txt
  ```

### Installation

1. Get a free API Key at [https://mapbox.com](https://mapbox.com)
2. Clone the repo
   ```sh
   git clone https://github.com/kevin-douglas/covid19project-backend.git
   ```
3. Enter your MapBox API in `temaples/map.html`
   ```js
   L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
   accessToken: '<insert API key here>'
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Edit /template/map.html and add your mapbox API key.
2. Run the csv-dl.py
3. Initialize your Django web server
4. Visit 127.0.0.1:8000/markers/map and enjoy the data!

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/kevin-douglas/covid19project-backend/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

## Project Link: [https://github.com/kevin-douglas/covid19project-backend/](https://github.com/kevin-douglas/covid19project-backend/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kevin-douglas/covid19project-backend.svg?style=for-the-badge
[contributors-url]: https://github.com/kevin-douglas/covid19project-backend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kevin-douglas/covid19project-backend.svg?style=for-the-badge
[forks-url]: https://github.com/kevin-douglas/covid19project-backend/network/members
[stars-shield]: https://img.shields.io/github/stars/kevin-douglas/covid19project-backend?style=for-the-badge
[stars-url]: https://github.com/kevin-douglas/covid19project-backend/stargazers
[issues-shield]: https://img.shields.io/github/issues/kevin-douglas/covid19project-backend.svg?style=for-the-badge
[issues-url]: https://github.com/kevin-douglas/covid19project-backend/issues
[license-shield]: https://img.shields.io/github/license/kevin-douglas/covid19project-backend.svg?style=for-the-badge
[license-url]: https://github.com/kevin-douglas/covid19project-backend/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/
[product-screenshot]: images/screenshot.png
