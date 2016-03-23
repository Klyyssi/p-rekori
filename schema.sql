CREATE TABLE IF NOT EXISTS snippet_types_ (
    id_ integer PRIMARY KEY,
    name_ text
);

CREATE TABLE IF NOT EXISTS snippets_ (
    id_ integer PRIMARY KEY,
    type_ integer NOT NULL,
    content_ text NOT NULL
);

CREATE TABLE IF NOT EXISTS notes_ (
    note_ integer,
    snippet_ integer,
    PRIMARY KEY (note_, snippet_)
) WITHOUT ROWID;
