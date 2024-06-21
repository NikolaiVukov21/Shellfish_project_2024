drop schema if exists test_4;
create schema test_4;
use test_4;


create table people
(
    Username     varchar(64) not null
        primary key,
    Password     varchar(64) null,
    Time_Created timestamp   not null
);

create table raw_files
(
    Raw_File_ID   int auto_increment
        primary key,
    Username      varchar(64)   not null,
    Filepath      varchar(2048) not null,
    Size          varchar(64)   not null,
    Type          varchar(64)   not null,
    Extension     varchar(64)   not null,
    Notes         varchar(2048) not null,
    Width         int           not null,
    Height        int           not null,
    Time_Uploaded timestamp     not null,
    constraint username_2
        foreign key (Username) references people (Username)
);

create index raw_files_people_Username_fk
    on raw_files (Username);

create table roboflow
(
    Roboflow_ID int auto_increment
        primary key,
    Api_Key     varchar(64) not null,
    Workspace   varchar(64) null,
    Project     varchar(64) null,
    Version     int         null,
    Download    varchar(64) null,
    Username    varchar(64) not null,
    constraint roboflow_ibfk_1
        foreign key (Username) references people (Username)
);

create table models
(
    Model_ID               int auto_increment
        primary key,
    Timestamp_Created      timestamp     not null,
    Model_Points_Path      varchar(64)   not null,
    Version                int           not null,
    Hyperparams            varchar(2048) not null,
    Model_Type             varchar(64)   not null,
    Width_Training_Images  int           not null,
    Height_Training_Images int           not null,
    Roboflow_ID            int           not null,
    constraint models_roboflow_Roboflow_ID_fk
        foreign key (Roboflow_ID) references roboflow (Roboflow_ID)
);

create table annotated_files
(
    Raw_File_ID        int           not null,
    Model_ID           int           not null,
    Annotated_Filepath varchar(2048) not null,
    Time_to_Annotate   time          not null,
    Notes              varchar(2048) not null,
    Ann_File_ID        int auto_increment
        primary key,
    constraint annotated_files_pk
        unique (Raw_File_ID, Model_ID),
    constraint annotated_files_models_Model_ID_fk
        foreign key (Model_ID) references models (Model_ID),
    constraint annotated_files_raw_files_Raw_File_ID_fk
        foreign key (Raw_File_ID) references raw_files (Raw_File_ID)
);

create table annotated_photos
(
    Ann_File_ID       int not null,
    Number_of_Oysters int not null,
    constraint annotated_photos_annotated_files_Ann_File_ID_fk
        foreign key (Ann_File_ID) references annotated_files (Ann_File_ID)
);

create table annotated_videos
(
    Ann_File_ID               int        not null
        primary key,
    Annotation_Rate           int        null,
    Tracing                   tinyint(1) null,
    Average_Number_of_Oysters float      not null,
    constraint annotated_videos_annotated_files_Ann_File_ID_fk
        foreign key (Ann_File_ID) references annotated_files (Ann_File_ID)
);

create table oysters_in_photo
(
    Ann_File_ID int not null,
    Confidence  int null,
    Coordinates int null,
    Class       int null,
    constraint oysters_in_photo_annotated_photos_Ann_File_ID_fk
        foreign key (Ann_File_ID) references annotated_photos (Ann_File_ID)
);

create index Username
    on roboflow (Username);

create table videos
(
    Raw_File_ID int        not null
        primary key,
    FPS         float      not null,
    Color_Order varchar(5) null,
    constraint videos_raw_files_Raw_File_ID_fk
        foreign key (Raw_File_ID) references raw_files (Raw_File_ID)
);

