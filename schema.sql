CREATE TABLE IF NOT EXISTS tag_categories_ (
    id_ integer PRIMARY KEY,
    name_ text
);

CREATE TABLE IF NOT EXISTS tags_ (
    id_ integer PRIMARY KEY,
    category_ integer, -- foreign key references tag_categories_
    name_ text NOT NULL
);

CREATE TABLE IF NOT EXISTS notes_ (
    id_ integer PRIMARY KEY,
    subject_ text,
    body_ text
);

CREATE TABLE IF NOT EXISTS note_tags_ (
    note_ integer NOT NULL, -- foreign key references notes_
    tag_ integer NOT NULL, -- foreign key references tags_
    PRIMARY KEY (note_, tag_)
) WITHOUT ROWID;
