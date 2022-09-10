DROP SCHEMA IF EXISTS hades;
CREATE SCHEMA hades;
USE hades;

CREATE TABLE role
(
    role_id     VARCHAR(36)  NOT NULL,
    name        VARCHAR(20)  NOT NULL,
    description VARCHAR(200) NOT NULL,
    PRIMARY KEY (role_id, name),
    CONSTRAINT name_UNIQUE
        UNIQUE (name),
    CONSTRAINT role_id_UNIQUE
        UNIQUE (role_id)
);

CREATE TABLE scope
(
    scope_id    VARCHAR(36)  NOT NULL,
    name        VARCHAR(20)  NOT NULL,
    description VARCHAR(200) NOT NULL,
    PRIMARY KEY (scope_id, name),
    CONSTRAINT name_UNIQUE
        UNIQUE (name),
    CONSTRAINT scope_id_UNIQUE
        UNIQUE (scope_id)
);

CREATE TABLE role_scope
(
    role_id       VARCHAR(36) NOT NULL,
    role_name     VARCHAR(20) NOT NULL,
    scope_id      VARCHAR(36) NOT NULL,
    scope_name    VARCHAR(20) NOT NULL,
    assign_date   DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    assign_status VARCHAR(10) NOT NULL DEFAULT 'ACTIVE',
    PRIMARY KEY (role_id, role_name, scope_id, scope_name),
    CONSTRAINT fk_role_has_scope_role1
        FOREIGN KEY (role_id, role_name) REFERENCES role (role_id, name),
    CONSTRAINT fk_role_has_scope_scope1
        FOREIGN KEY (scope_id, scope_name) REFERENCES scope (scope_id, name)
);

CREATE INDEX fk_role_has_scope_role1_idx
    ON role_scope (role_id, role_name);

CREATE INDEX fk_role_has_scope_scope1_idx
    ON role_scope (scope_id, scope_name);

CREATE TABLE user_role
(
    user_id   VARCHAR(36) NOT NULL,
    role_id   VARCHAR(36) NOT NULL,
    role_name VARCHAR(20) NOT NULL,
    assign_date   DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    assign_status VARCHAR(10) NOT NULL DEFAULT 'ACTIVE',
    PRIMARY KEY (role_id, role_name, user_id),
    CONSTRAINT fk_user_has_role_role1
        FOREIGN KEY (role_id, role_name) REFERENCES role (role_id, name)
);

CREATE INDEX fk_user_has_role_role1_idx
    ON user_role (role_id, role_name);
