<a name="readme-top"></a>


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

<h3 align="center">Fake Github Commit History</h3>

  <p align="center">
    a Pypi package to help fake github history
    <br />
    <br />
    <a href="https://github.com/Vish-04/fake-github-commit-history/issues">Report Bug</a>
    ·
    <a href="https://github.com/Vish-04/fake-github-commit-history/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A Pypi pakcage to fake github commit history

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local repo with faked history up and running follow these simple example steps.

### Prerequisites

Ensure you have python. Follow the steps on the official documentation https://www.python.org/downloads/

You can check what python version you have with the following command
  ```sh
  python --version
  ```
Git is also necessary to run the package. Follow the documentation to install Git: https://github.com/git-guides/install-git

### Installation

1. Upgrade pip 
   ```sh
   pip install --upgrade pip
   ```
2. Install fgch pip packages 
   ```sh
   pip install gh-commit-history
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
<br />
The fake github commit history generator has many different functionalities to produce various realistic and versatile commit frequencies
<br />
**General Usage**
<br />
1. Navigate to the location you wish to fake your history and enter python shell in terminal
<br />
Windows:
`python`
<br />
Mac/Linux:
<br />
`python3`

<br />
3. Import the module:

`>> from fgch.commit_generator import generate_commits`
<br />
3. Run the module:

`>> generate_commits()`
<br />
A new directory titled `github-history` with a file named `fake-history.txt` should have appeared after the sequence commences
<br />
_Including no parameters will run the default settings_
<br />
4. Create a GitHub Repository with a name of your choice (recommend github-history)
<br />
5. Push changes into the GitHub Repository
<br />
Navigate to the github-history directory
<br />
Windows:
<br />
`cd .\github-history\`
<br />
Mac/Linux:
<br />
`cd /github-history`
<br />

Connect remote to GitHub Repository 
<br />
`git remote add origin https://github.com/<your-user-name>/<your-repository-name>.git` Ex: `git remote add origin https://github.com/Vish-04/github-history.git`
<br />

Push to Repository
<br />
`git push -u origin master`
<br />

_**Reload your GitHub Profile, and your history should be changed!**_
<br />
**Parameters**

`commits_per_day` : type `String "int-int"`, default: `"0-3"`
<br />
_range between which the number of commits per day is chosen from_
<br />
`start_date` : type `String "MM/DD/YY"`, default: `None`
<br />
_start date of fake github history. If None, start date will be a year back from current date_
<br />
`end_date` : type `String "MM/DD/YY"`, default: `None`
<br />
_end date of fake github history. If None, end date will be the current date_
<br />
`workdays_only` : type `Boolean`, default: `False`
<br />
_restricts commits to only occur on weekdays_
<br />
`weekend_behavior` : type `Boolean`, default: `False`
<br />
_lowers commit frequency to 0-1 commits on weekends_
<br />
`working_hours` : type `String "int-int"`, default: `9-17`
<br />
_determines between what hours in military time to commit between_
<br />
`gradient` : type `String`, default: `None`
<br />
_increases commits per day closer to the higher number of commit range over time - choose between 'linear', 'exponential', 'bursts'_
- linear: linearly increases commits per day
- exponential: exponentially increases commits per day
- bursts: increases and decreases commits per day in batches of 3 weeks, mimicking sprints
<br />
`no_commit_percentage` : type `Float`, default: `0`
<br />
_float between 0 and 1 that determines what percentage of history to not fake commits too_




<p align="right">(<a href="#readme-top">back to top</a>)</p>




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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Vishwa Akkati - [LinkedIn](https://linkedin.com/in/vishwa-akkati) - vakkati@ucdavis.edu

Project Link: [https://github.com/Vish-04/fake-github-commit-history](https://github.com/Vish-04/fake-github-commit-history)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Vish-04/fake-github-commit-history.svg?style=for-the-badge
[contributors-url]: https://github.com/Vish-04/fake-github-commit-history/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vish-04/fake-github-commit-history.svg?style=for-the-badge
[forks-url]: https://github.com/Vish-04/fake-github-commit-history/network/members
[stars-shield]: https://img.shields.io/github/stars/Vish-04/fake-github-commit-history.svg?style=for-the-badge
[stars-url]: https://github.com/Vish-04/fake-github-commit-history/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vish-04/fake-github-commit-history.svg?style=for-the-badge
[issues-url]: https://github.com/Vish-04/fake-github-commit-history/issues
[license-shield]: https://img.shields.io/github/license/Vish-04/fake-github-commit-history.svg?style=for-the-badge
[license-url]: https://github.com/Vish-04/fake-github-commit-history/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/vishwa-akkati
[product-screenshot]: images/screenshot.png
