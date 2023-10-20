# Command line for the win
## General Objectives
- A README.md file, at the root of the folder of the project, is mandatory
- This project will be manually reviewed.
- As each task is completed, the name of that task will turn green
- Create a screenshot, showing that you completed the required levels
- Push this screenshot with the right name to GitHub, in either the PNG or JPEG format

## Specific Objectives
- In addition to completing the project tasks and submitting the required screenshots to GitHub,
you are also required to demonstrate the use of the SFTP (Secure File Transfer Protocol)
command-line tool to move your local screenshots to the sandbox environment.

## Steps Followed while Uploading the Files through SFTP
1. Sandbox Page from the Intranet, and chose Ubuntu 20.04
2. On the Local machine (Windows 10), entered the commandline interface (Powershell)
    and navigated to the folder that contains the files
3. First tested ssh in the terminal to connect to the sandbox
4. Then used ```sftp <username>@<hostname>```, then entered the ```password```.
5. Navigated to ```/root```, created the folders ```/root/alx-system_engineering-devops``` and
    ```/root/alx-system_engineering-devops/command_line_for_the_win```
6. Confirmed the current remote folder with ```pwd``` and also the local folder with ```lpwd```
7. The used ```put *``` and the files were uploaded to the sandbox
