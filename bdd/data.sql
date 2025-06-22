INSERT INTO theme (name) VALUES
('Motivation'),
('Sagesse'),
('Humour');

INSERT INTO auteur (nom) VALUES
('Winston Churchill'),
('Albert Einstein'),
('Oscar Wilde');

-- Winston Churchill (id = 1)
INSERT INTO citation (auteur_id, theme_id, citation) VALUES
(1, 1, 'Le succès, c’est d’aller d’échec en échec sans perdre son enthousiasme.'),
(1, 2, 'Un pessimiste voit la difficulté dans chaque opportunité, un optimiste voit l’opportunité dans chaque difficulté.'),
(1, 3, 'Je suis facilement satisfait du meilleur.');

-- Albert Einstein (id = 2)
INSERT INTO citation (auteur_id, theme_id, citation) VALUES
(2, 1, 'La vie, c’est comme une bicyclette, il faut avancer pour ne pas perdre l’équilibre.'),
(2, 2, 'La folie, c’est de faire toujours la même chose et de s’attendre à un résultat différent.'),
(2, 3, 'Deux choses sont infinies : l’univers et la stupidité humaine ; et je ne suis pas sûr de l’univers.');

-- Oscar Wilde (id = 3)
INSERT INTO citation (auteur_id, theme_id, citation) VALUES
(3, 1, 'Soyez vous-même, les autres sont déjà pris.'),
(3, 2, 'L’expérience est simplement le nom que nous donnons à nos erreurs.'),
(3, 3, 'Je peux résister à tout sauf à la tentation.');
