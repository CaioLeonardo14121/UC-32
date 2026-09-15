CREATE TABLE `autores` (
  `id_autor` integer PRIMARY KEY,
  `nome` varchar(100),
  `nacionalidade` varchar(50)
);

CREATE TABLE `livros` (
  `id_livro` integer PRIMARY KEY,
  `titulo` varchar(150),
  `ano_publicacao` integer,
  `genero` varchar(50),
  `quantidade` integer,
  `id_autor` integer
);

CREATE TABLE `leitores` (
  `id_leitor` integer PRIMARY KEY,
  `nome` varchar(100),
  `email` varchar(100),
  `telefone` varchar(20)
);

CREATE TABLE `emprestimos` (
  `id_emprestimo` integer PRIMARY KEY,
  `id_livro` integer,
  `id_leitor` integer,
  `data_emprestimo` date,
  `data_devolucao` date
);

ALTER TABLE `livros` ADD FOREIGN KEY (`id_autor`) REFERENCES `autores` (`id_autor`);

ALTER TABLE `emprestimos` ADD FOREIGN KEY (`id_livro`) REFERENCES `livros` (`id_livro`);

ALTER TABLE `emprestimos` ADD FOREIGN KEY (`id_leitor`) REFERENCES `leitores` (`id_leitor`);
