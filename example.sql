-- Usage:
--  $ rm parekori.db
--  $ sqlite3 parekori.db < schema.sql
--  $ sqlite3 parekori.db < example.sql

INSERT INTO tags_ (id_, name_) VALUES
    (1, 'mathematics'), (2, 'geometry'), (3, 'triangle');

INSERT INTO notes_ (id_, subject_, body_) VALUES
    (1, 'Equilateral triangle', 'In geometry, an equilateral triangle is a triangle in which all three sides are equal. In the familiar Euclidean geometry, equilateral triangles are also equiangular; that is, all three internal angles are also congruent to each other and are each 60°. They are regular polygons, and can therefore also be referred to as regular triangles.[1]' || CHAR(0xA,0xA) || '[1] https://en.wikipedia.org/wiki/Equilateral_triangle');

INSERT INTO note_tags_ (note_, tag_) VALUES (1, 1), (1, 2), (1, 3);

INSERT INTO notes_ (id_, subject_, body_) VALUES
    (2, 'Morley''s trisector theorem', 'In plane geometry, Morley''s trisector theorem states that in any triangle, the three points of intersection of the adjacent angle trisectors form an equilateral triangle, called the first Morley triangle or simply the Morley triangle. The theorem was discovered in 1899 by Anglo-American mathematician Frank Morley. It has various generalizations; in particular, if all of the trisectors are intersected, one obtains four other equilateral triangles.[1]' || CHAR(0xA,0xA) || '[1] https://en.wikipedia.org/wiki/Morley''s_trisector_theorem');

INSERT INTO note_tags_ (note_, tag_) VALUES (2, 1), (2, 2), (2, 3);
