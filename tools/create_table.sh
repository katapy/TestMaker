
APP_NAME=test-maker
POD_NAME=`kubectl get pod --namespace=$APP_NAME | grep $APP_NAME | awk '{print $1}'`

# Get Secret value
POSTGRES_DB=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_DB | awk '{print $2}' | base64 --decode`
POSTGRES_PASSWORD=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_PASSWORD | awk '{print $2}' | base64 --decode`
POSTGRES_USER=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_USER | awk '{print $2}' | base64 --decode`

kubectl exec -i $POD_NAME -c postgres --namespace=$APP_NAME -- bash <<'EOC'
PSQL_URI="postgresql://localhost/$POSTGRES_DB?user=$POSTGRES_USER"
echo "Connect RDB"
psql $PSQL_URI

create table table_header (
    table_name varchar(100),
    column_name varchar(100),
    display_name varchar(100),
    PRIMARY KEY (table_name, column_name)
);

create table person (
    id SERIAL NOT NULL, 
    name varchar(100),
    PRIMARY KEY (id)
);

create table change_log (
    change_log_id SERIAL NOT NULL, 
    created_user_id integer,
    updated_user_id integer,
    created_date timestamp,
    updated_date timestamp,
    PRIMARY KEY (change_log_id)
);

-- app_package
create table app_user (
    id SERIAL NOT NULL, 
    name varchar(100),
    password varchar(100),
    mail varchar(100),
    PRIMARY KEY (id)
);

create table app (
    app_id SERIAL NOT NULL, 
    app_name varchar(100),
    PRIMARY KEY (app_id)
);

create table app_user_relation (
    app_user_relation_id SERIAL NOT NULL, 
    user_id integer,
    app_id integer,
    PRIMARY KEY (app_user_relation_id),
    foreign key (user_id) references app_user(id), 
    foreign key (app_id) references app(app_id)
);

-- app_infomation_package
create table perspective (
    perspective_id SERIAL NOT NULL, 
    perspective_name varchar(100),
    perspective_detail text,
    is_setting boolean,
    PRIMARY KEY (perspective_id)
);

create table usecase (
    usecase_id SERIAL NOT NULL, 
    usecase_name varchar(100),
    usecase_detail text,
    PRIMARY KEY (usecase_id)
);

create table app_usecase_perspective_relation (
    app_usecase_perspective_relation_id SERIAL NOT NULL, 
    app_id integer,
    usecase_id integer,
    perspective_id integer,
    PRIMARY KEY (app_usecase_perspective_relation_id),
    foreign key (app_id) references app(app_id), 
    foreign key (usecase_id) references usecase(usecase_id), 
    foreign key (perspective_id) references perspective(perspective_id)
);

-- test_summary_package
create table test_summary (
    test_summary_id SERIAL NOT NULL, 
    change_log_id integer,
    test_summary_name varchar(100),
    PRIMARY KEY (test_summary_id)
);

create table app_test_summary_relation (
    app_test_summary_relation_id SERIAL NOT NULL, 
    app_id integer,
    test_summary_id integer,
    PRIMARY KEY (app_test_summary_relation_id),
    foreign key (app_id) references app(app_id), 
    foreign key (test_summary_id) references test_summary(test_summary_id)
);

create table test_status (
    test_status_id integer,
    test_status varchar(100),
    PRIMARY KEY (test_status_id)
);

create table test_flow (
    test_flow_id SERIAL NOT NULL,
    test_summary_id integer,
    change_log_id integer,
    test_status_id integer,
    test_name varchar(100),
    PRIMARY KEY (test_flow_id),
    foreign key (test_summary_id) references test_summary(test_summary_id),
    foreign key (change_log_id) references change_log(change_log_id), 
    foreign key (test_status_id) references test_status(test_status_id)
);

create table test_perspective (
    test_perspective_id SERIAL NOT NULL,
    perspective_id integer,
    test_flow_id integer,
    PRIMARY KEY (test_perspective_id),
    foreign key (perspective_id) references perspective(perspective_id), 
    foreign key (test_flow_id) references test_flow(test_flow_id)
);

create table testcase (
    testcase_id SERIAL NOT NULL,
    test_flow_id integer,
    usecase_id integer,
    test_number integer,
    expected text,
    PRIMARY KEY (testcase_id),
    foreign key (test_flow_id) references test_flow(test_flow_id),
    foreign key (usecase_id) references usecase(usecase_id)
)

\dt

EOC
