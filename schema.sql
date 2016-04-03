CREATE TABLE IF NOT EXISTS snippet_types_ (
    id_ integer PRIMARY KEY,
    name_ text
);

CREATE TABLE IF NOT EXISTS snippets_ (
    id_ integer PRIMARY KEY,
    type_ integer NOT NULL, -- foreign key references snippet_types_
    content_ text NOT NULL
);

CREATE TABLE IF NOT EXISTS notes_ (
    id_ integer PRIMARY KEY,
    summary_ integer -- foreign key references snippets_
);

CREATE TABLE IF NOT EXISTS note_snippets_ (
    note_ integer, -- foreign key references notes_
    snippet_ integer, -- foreign key references snippets_
    PRIMARY KEY (note_, snippet_)
) WITHOUT ROWID;
