# IPL Buddy

<h2>Project Development Journal</h2>

<h3><code style="color:blue">Tech stack</code></h3>

<div align="center">
    <table>
        <tr align="center">
            <th>Stack</th>
            <th>Name</th>
        </tr>
        <tr align="center">
            <td>Chatbot platform</td>
            <td>Google Dialogflow Console</td>
        </tr>
        <tr align="center">
            <td>Database</td>
            <td>MySQL</td>
        </tr>
        <tr align="center">
            <td>Backend framework</td>
            <td>FastAPI</td>
        </tr>
        <tr align="center">
            <td>Production Database</td>
            <td>aiven.io</td>
        </tr>
        <tr align="center">
            <td>Production server</td>
            <td>render.com</td>
        </tr>
        <tr align="center">
            <td>Integration site</td>
            <td>Huggingface</td>
        </tr>
    </table>
</div>

<h3><code style="color:blue">Codebase</code></h3>
<strong>I handled the backend api calling using fastapi. All the files that are used to prepare and maintain the chatbot can be found <a href='https://github.com/Neloy-Barman/IPL-Chatbot/tree/backend'>here</a>. I'm adding a short description of all the files and folders.</strong>

<h4>👉 main.py</h4>
<strong>This is the main .py file from where the backend handling starts.</strong>

<h4>👉 generic_helpers.py</h4>
<strong>There are some values, dictionaries and methods that are used in many files. So, all of them are placed here and those are imported from this file.</strong>

<h4>👉 config.py</h4>
<strong>As the conversation progresses, some parameters are to be stored, that are needed to fetch final data. These are saved in a dictionary with the session id as the key.</strong>

<h4>👉 db_helpers</h4>
<strong>All these *.py files within this folder are used to fetch data from the database server. Different files contain methods that read from the database and returns relatable data needed.</strong>
<div align="center">
    <table align="center">
        <tr align="center">
            <th>File Name</th>
            <th>Fetch Handling to database</th>
        </tr>
        <tr align="center">
            <td>db_connection</td>
            <td>Creates and close connection to the database.</td>
        </tr>
        <tr align="center">
            <td>dates_db</td>
            <td>Particular session start date and end date.</td>
        </tr>
        <tr align="center">
            <td>match_db</td>
            <td>toss decision, winning runs, winning wickets, match result type and dls method.</td>
        </tr>
        <tr align="center">
            <td>player_of_the_match_db</td>
            <td>player of the match.</td>
        </tr>
        <tr align="center">
            <td>seasons_db</td>
            <td>available unique sessions.</td>
        </tr>
        <tr align="center">
            <td>teams_db</td>
            <td>both teams, match winner and toss winner teams.</td>
        </tr>
        <tr align="center">
            <td>umpires_db</td>
            <td>first umpire, second umpire and both umpires.</td>
        </tr>
        <tr align="center">
            <td>venues_db</td>
            <td>venues for the particular session and date.</td>
        </tr>
    </table>
</div>


<h4>👉 intent_helpers</h4>
<strong>*.py Files here are used to handling data fetching and generating responses of the chatbot based on particular intent.</strong>
<div align="center">
   <table align="center">
        <tr align="center">
            <th>File Name</th>
            <th>Backend handling for intent</th>
        </tr>
        <tr align="center">
            <td>date_helper</td>
            <td>Date</td>
        </tr>
        <tr align="center">
            <td>match_info_helper</td>
            <td>Match Info and Match Info Next.</td>
        </tr>
        <tr align="center">
            <td>player_of_the_match_helper</td>
            <td>Player of the Match.</td>
        </tr>
        <tr align="center">
            <td>season_helper</td>
            <td>Season.</td>
        </tr>
        <tr align="center">
            <td>team_info_helper</td>
            <td>Team Info and Team Info Next.</td>
        </tr>
        <tr align="center">
            <td>umpire_info_helper</td>
            <td>Umire Info and Umpire Info Next.</td>
        </tr>
        <tr align="center">
            <td>venues_helper</td>
            <td>Venue.</td>
        </tr>
    </table>
</div>


<h4>👉 requirements.txt</h4>
<strong>It contains information of all the dependencies with their particular versions installed and used to create and maintain the app.</strong>

<h4>👉 .gitignore</h4>
<strong>It has all the file patterns that needs to be ignored while pushing to the github.</strong>






<h3><code style="color:blue">Integration</code></h3>

<strong>I integrated my chatbot using google dialoglfow messenger api. I created a basic UI just for the sake of chatbot testing and deployed the website in huggingface. You can check it out <a href="https://huggingface.co/spaces/nelbarman053/IPL-Chat-Buddy">here</a>. Below the code snippet is given, in case you want to integrate and test: - </strong>

    <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
    <df-messenger
    intent="WELCOME"
    chat-title="IPL_BOT"
    agent-id="cc8dfc8c-36c0-420e-9c7b-aeb2ba566a1c"
    language-code="en"
    ></df-messenger>

<h3><code style="color:blue">Conversation Flow Diagrams</code></h3>

<h4>Team Info</h4>
<div><img src="assets/team_info.png"></div>

<h4>Match Info</h4>
<div><img src="assets/match_info.png"></div>

<h4>Umpire Info</h4>
<div><img src="assets/umpire_info.png"></div>

<h4>Player of the Match</h4>
<div><img src="assets/player_of_the_match.png"></div>


<h3><code style="color:blue">Conversation snaps</code></h3>

<table>
    <tr>
        <td><img src="assets/1st.png" height="400"></td>
        <td><img src="assets/2nd.png" height="400"></td>
    </tr>
     <tr>
        <td><img src="assets/3rd.png" height="400"></td>
        <td><img src="assets/4th.png" height="400"></td>
    </tr>
      <tr>
        <td><img src="assets/5th.png" height="400"></td>
    </tr>
</table>




