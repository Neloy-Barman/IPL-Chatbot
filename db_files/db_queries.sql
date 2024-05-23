
-- Database Creation
CREATE DATABASE IF NOT EXISTS `ipldb`;-- 

-- Using Created Database 
USE ipldb;

-- Creating table 
CREATE TABLE iplstat (
	sid INT AUTO_INCREMENT PRIMARY KEY,
	season INT,
    city VARCHAR(255),
    date DATE,
    team1 VARCHAR(255),
    team2 VARCHAR(255),
    toss_winner VARCHAR(255),
    toss_decision VARCHAR(50),
    result VARCHAR(50),
	dl_applied INT,
    winner VARCHAR(255),
    win_by_runs INT, 
    win_by_wickets INT,
    player_of_match VARCHAR(255),
    venue VARCHAR(255),
    umpire1 VARCHAR(255),
    umpire2 VARCHAR(255)
);

-- Dropping Table
DROP TABLE IF EXISTS iplstat;

-- Value Insertion into table
INSERT INTO iplstat(season, city, date, team1, team2, toss_winner, toss_decision, result, dl_applied, winner, win_by_runs, win_by_wickets, player_of_match, venue, umpire1, umpire2)
VALUES (2017, 'Hyderabad', '2017-04-05', 'Sunrisers Hyderabad', 'Royal Challengers Bangalore', 'Royal Challengers Bangalore', 'field', 'normal', 0, 'Sunrisers Hyderabad', 35, 0, 'Yuvraj Singh', 'Rajiv Gandhi International Stadium, Uppal', 'AY Dandekar', 'NJ Llong');

INSERT INTO iplstat(season, city, date, team1, team2, toss_winner, toss_decision, result, dl_applied, winner, win_by_runs, win_by_wickets, player_of_match, venue, umpire1, umpire2)
VALUES (2019, 'Hyderabad', '12/05/19', 'Mumbai Indians', 'Chennai Super Kings', 'Mumbai Indians', 'bat', 'normal', 0, 'Mumbai Indians', 1, 0, 'JJ Bumrah', 'Rajiv Gandhi Intl. Cricket Stadium', 'Nitin Menon', 'Ian Gould');

-- Selection from table
SELECT * FROM iplstat;
