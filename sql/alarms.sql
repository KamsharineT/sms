CREATE DATABASE IF NOT EXISTS alarms;

use alarms;

CREATE TABLE if not exists alarms_det (alarmid int NOT NULL AUTO_INCREMENT,
    stnameid varchar(50) NOT NULL,
    alarmname varchar(500) NOT NULL,
    alarmcreated DATETIME,
    date DATETIME,
    smssent varchar(6),
    PRIMARY KEY (alarmid));


CREATE TABLE if not exists stations_det (stid int NOT NULL AUTO_INCREMENT,
    stname varchar(50) NOT NULL,
    stnameid varchar(10) NOT NULL,
    pH_min float,
    pH_max float,
    Chladj_min float,
    Chladj_max float,
    DO_min float,
    DO_max float,
    Conductivity_min float,
    Conductivity_max float,
    Turbidity_min float,
    Turbidity_max float,
    PRIMARY KEY (stid));


INSERT INTO stations_det (stid, stname,stnameid, pH_min,pH_max, chladj_min,chladj_max,DO_min,DO_max,Conductivity_min,Conductivity_max,Turbidity_min,Turbidity_max) 
VALUES(1, 'Alexandra Canal','SE565', 5.74, 9.5, 0.0,37.72,0.0,8.9,54.5,482.5,1.0,410.89),
    (2, 'Bedok','SE501', 5.95, 10.50,0.0,21.82,6.02,10.87,182,286,0,1.6),
    (3, 'Bedok Wetwell','SE540', 6.22, 7.9,0,38.28,0.0,9.95,183.5,251.5,0.0,87.7),
    (5, 'Bishan Park 2','SE533', 4.5, 9.04, 1.6,29.65,2.41,9.85,87.5,379.5,0,116.65),
    (6, 'Buangkok East Drive','SE509', 5.83, 8.63, 0.0,62.89 ,0.0,11.12,75,843,0.0,592.35),
    (7, 'Bukit Timah 2nd Diversion Canal_Jalan Tenteram','SE552', 6.36, 7.8, 0.0,48.32,0.0,10.69,0.0,462.0,0.0,144.95),
    (8, 'Geylang River_Dunman Road','SE534', 6.71, 7.79, 0.0,64.96,0.0,7.5,0.0,931.5,0.0,96.2),
    (9, 'Geylang River_Tanjong Rhu Road','SE510', 6.5, 8.1, 0.0,44.70,0.0,10.47,0,1023.5,0.0,108.1),
    (10, 'Jurong Canal','SE542', 6.96, 8.72, 0.0,68.21,0.0,9.17,98,746,0.0,710.3),
    (11, 'Jurong Lake','SE511', 6.67, 8.02, 0.0,48.45,0.0,9.64,32,552,30,281.2),
    (12, 'Kallang Basin','SE512', 6.57, 8.33, 0.0,77.46,1.2,10.0,116,460,0.0,350.76),
    (13, 'Kallang River_Braddell Road','SE563', 6.68, 7.8, 0.0,41.80,0.0,8.5,107.38,362.77,0.0,115.93),
    (14, 'Kallang River_Serangoon Road','SE514', 6.0, 8.1, 0.0,22.47,0.85,8.5,69.5,369.5,0.0,43.25),
    (15, 'KR2US','SE543', .07, 9.67, 2.31, 32.34, 7.09, 10.13, 55.0, 191.0, 0.0, 30.95),
    (16, 'Kranji 1','SE515', .76, 10.12, 0.0, 28.35, 5.09, 12.13, 132.0, 380.0, 0.0, 60.7),
    (17, 'Kranji 2','SE502', 6.34, 10.3, 0.0, 47.07, 5.27, 11.83, 177.5, 301.5, 0.0, 58.25),
    (18, 'Lower Peirce','SE516', 6.45, 7.97, 0.0, 24.17, 6.0, 9.4, 103.0, 223.0, 0.0, 34.55),
    (19, 'Lower Seletar','SE565', 5.74, 9.53, 0.0, 37.73, 0.0, 8.9, 54.5, 482.5, 0.0, 410.89),
    (20, 'MacRitchie','SE517', 4.59, 9.31, 0.0, 30.3, 8.1, 9.17, 16.0, 56.0, 0.2, 7.4),
    (21, 'Marina Bay','SE518', 6.51, 8.83, 0.0, 48.82, 3.43, 9.72, 257.0, 441.0, 0.0, 293.7),
    (22, 'Marina Channel','SE504', 6.74, 8.62, 0.0, 38.77, 4.14, 10.22, 132.5, 576.5, 0.0, 56.65),
    (23, 'MR2UP','SE521', 6.8, 9.2, 0.0, 30.29, 3.14, 16.34, 204.0, 316.0, 0.0, 2.4),
    (24, 'Murai','SE522', 6.86, 9.78, 0.0, 56.2, 6.06, 11.06, 40.0, 88.0, 0.0, 11.45),
    (25, 'Neo Tiew Lane 1_NT 1','SE553', 6.72, 7.44, 0.46, 46.98, 0.0, 3.84, 121.5, 885.5, 0.0, 499.35),
    (26, 'Neo Tiew Lane 1_NT 2','SE560', 6.95, 7.56, 0.0, 63.57, 0.0, 7.56, 218.25, 757.05, 0.0, 695.7),
    (27, 'Neo Tiew Lane 2','SE545', 6.8, 7.92, 0.0, 52.55, 0.0, 7.56, 91.0, 1099.0, 0.0, 170.16),
    (28, 'Pandan','SE505', 7.34, 9.77, 0.0, 34.73, 6.26, 9.89, 160.5, 444.5, 0.0, 27.9),
    (29, 'Pandan 3','SE547', 7.56, 9.69, 2.45, 17.94, 5.8, 11.53, 186.0, 346.0, 0.0, 23.1),
    (30, 'Pandan Canal','SE523', 6.64, 7.56, 0.0, 58.74, 0.0, 8.05, 0.0, 769.0, 0.0, 327.9),
    (31, 'Pang Sua Canal','SE548', 6.72, 8.36, 0.0, 89.83, 3.24, 11.12, 157.5, 425.5, 0.0, 424.05),
    (32, 'Pang Sua Pond','SE539', 6.56, 8.0, 0.0, 62.91, 3.68, 10.48, 56.5, 300.5, 0.0, 109.9),
    (33, 'Pelton Canal','SE535', 6.83, 7.71, 0.0, 48.33, 0.0, 5.69, 0.0, 667.7, 0.0, 208.74),
    (34, 'Poyan','SE506', 7.37, 9.39, 1.91, 27.56, 6.42, 10.26, 192.5, 508.5, 0.0, 50.75),
    (35, 'PR2UP','SE520', 6.58, 9.94, 0.0, 24.69, 7.45, 9.48, 208.5, 260.5, 0.0, 9.95),
    (36, 'Pulau Tekong','SE507', 4.56, 8.44, 17.11, 74.79, 7.65, 9.41, 18.0, 34.0, 0.0, 45.0),
    (37, 'Punggol Waterway_Edgedale Plains','SE555', 6.7, 8.7, 0.0, 22.8, 0.84, 10.4, 188.5, 488.5, 0.0, 54.85),
    (38, 'Punggol Waterway_Punggol Way','SE556', 6.45, 9.12, 0.0, 26.8, 0.0, 11.22, 130.5, 558.5, 0.0, 116.15),
    (39, 'Punggol','SE519', 6.23, 9.91, 0.0, 30.68, 3.23, 12.19, 241.0, 561.0, 0.0, 117.0),
    (40, 'PWW','SE536', 6.44, 9.51, 9.56, 34.79, 0.0, 11.48, 46.0, 508.0, 0.0, 71.8),
    (42, 'Sarimbun','SE531', 6.62, 8.1, 1.44, 12.11, 5.88, 9.36, 124.0, 324.0, 0.0, 21.7),
    (58, 'Turut Track Canal','SE544', 7.03, 7.67, 0.0, 39.39, 0.0, 12.33, 217.0, 953.0, 0.0, 316.2),
    (59, 'Upper Peirce','SE508', 5.55, 9.66, 0.0, 34.56, 0.0, 16.09, 178.5, 302.5, 0.0, 2.1),
    (60, 'Upper Seletar','SE527', 6.2, 8.28, 0.0, 27.68, 4.94, 11.26, 57.0, 145.0, 0.0, 24.85),
    (61, 'Whampoa River','SE537', 6.64, 8.0, 0.0, 57.51, 0.0, 12.52, 47.62, 621.03, 0.0, 132.25),
    (62, 'Whampoa River_Whampoa CC','SE564', 6.59, 7.71, 0.0, 47.56, 0.0, 6.24, 47.5, 571.5, 0.0, 67.5),
    (63, 'Yishun Pond','SE528', 6.74, 7.94, 0.0, 107.75, 0.48, 12.68, 66.0, 482.0, 0.0, 269.95)

    (41, 'Rochor Canal','SE581', 6.76, 7.45, 0.0, 50.59, 0.0, 2.87, 160.0, 536.0, 0.0, 221.98),
    
    (43, 'Serangoon','SE524', 6.0, 9.6, 6.7,195.9,0.1,11.2,82.6,845.3,0.1,50),
    (44, 'Singapore River','SE525', 7.07, 8.11, 4.53, 36.72, 0.88, 9.72, 156.0, 396.0, 0.0, 340.72),
    (45, 'Sungei Lanchar','SE541', 6.0, 9.0, 0.1,40,0.3,9.5,34.9,566.4,0.01,85.5),
    (46, 'Sungei Mandai Kechil','SE532', 5.9, 9.0, 0.02,40,0.5,10.7,28.0,260.8,0.02,50.8),
    (47, 'Sungei Peng Siang Finger 1','SE549', 5.6, 9.0, 0.02,54.2,0.1,10.9,123.8,432.3,0.3,200),
    (48, 'Sungei Peng Siang Finger 2','SE550', 6.0, 9.0, 0.7,40,0.1,9.3,133.6,399.2,1.1,50),
    (49, 'Sungei Peng Siang Finger 3','SE551', 6.0, 9.0, 0.01,40,0.1,9.3,160.6,352.6,2.6,200),
    (50, 'Sungei Petai','SE559', 6.0, 9.0, 0.09,40,3.0,8.3,38.6,587.4,1.0,200),
    (51, 'Sungei Pinang','SE558', 6.0, 9.0, 0.01,40,0.1,9.1,45.2,466.3,0.1,200),
    (52, 'Sungei Punggol_Gerald Drive','SE554', 6.0, 9.0, 0.06,40,0.1,11.8,97.9,430.9,0.05,54.1),
    (53, 'Sungei Punggol_H2O Residence','SE562', 6.0, 9.0, 0.01,40,2.7,7.5,47.9,466.8,0.1,52.6),
    (54, 'Sungei Serangoon_Hougang Ave 7','SE557', 6.0, 9.0, 1.3,40,0.1,12.9,114.9,453.3,1.0,178.2),
    (55, 'Sungei Tampines','SE546', 6.0, 9.0, 0.001,40,0.1,11.4,40.3,704.3,0.6,85.1),
    (56, 'Sungei Ulu Pandan','SE561', 6.0, 9.0, 0.03,40,0.1,8.9,106.7,351.0,0.3,176.7),
    (57, 'Tengeh','SE526', 6.0, 9.6, 4.0,131.7,3.0,9.9,149.6,320.8,10.4,50),

    ;