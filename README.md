# EmergencyResponseGuide
ASU Emergency Response Guide App for 2016 CS Capstone.

# Set up
The following steps will get your environment all ready for development.

1. Install babun. You can download it [here](http://babun.github.io). _babun is a linux-looking terminal that will allow us to run useful commands that will work the same across all of our environments._
2. Install the latest version of Intel XDK, download [here](https://software.intel.com/en-us/intel-xdk)
3. Open up babun and navigate (`cd`) to where you want your source code to live. Change the following command to where you want to go. Run something akin to this to put the repository in your documents folder:
  ```
  cd /c/Users/<Your Username>/Documents/
  ```
  (Note that this directory inside babun is equivalent to `C:/Users/<Your Username>/Documents/` in Windows)

4. Change your name and email so that git is configured. Visit https://github.com/settings/profile to make sure they match what you use on GitHub.
  ```
  git config --global user.name "your name"
  git config --global user.email "your@email.com"
  ```

5. Clone our repository with this command:
  ```
  git clone https://github.com/ERG-Capstone/EmergencyResponseGuide.git
  ```
  This will create a folder called `EmergencyResponseGuide`. It may take a few moments to download. Congratulations, you now have a copy of our project inside a git repo on your computer.

6. Switch to the `EmergencyResponseGuide` directory:
  ```
  cd EmergencyResponseGuide
  ```

7. Let's make sure we have Python installed:
  ```
  pact install python
  ```

8. Run the following command to install the required python libraries:
  ```
  make install_deps
  ```
  This installs all of the dependencies listed in the `requirements.txt` file.

9. Test that all of the setup steps worked by running:
  ```
  make build
  ```

10. If that worked, you should be able to open and view the project in Intel XDK. Let me (Spencer) know if you run into any issues.

# IMPORTANT: Dev Instructions
WIP

## Contributors
- [Spencer Bywater](https://github.com/spencerbyw)
- [Dominique Fajardo](https://github.com/dnfajard)
- [Garett Winkler](https://github.com/garettwinkler)
- Garrett Decker
