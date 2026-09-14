CREATE TABLE `clientes` (
  `id_cliente` int PRIMARY KEY,
  `nome` varchar(255),
  `email` varchar(255),
  `telefone` varchar(255)
);

CREATE TABLE `produtos` (
  `id_produto` int PRIMARY KEY,
  `nome` varchar(255),
  `preco` decimal,
  `estoque` int
);

CREATE TABLE `pedidos` (
  `id_pedido` int PRIMARY KEY,
  `id_cliente` int,
  `data_pedido` date,
  `valor_total` decimal
);

CREATE TABLE `itens_pedido` (
  `id_item` int PRIMARY KEY,
  `id_pedido` int,
  `id_produto` int,
  `quantidade` int,
  `subtotal` decimal
);

ALTER TABLE `pedidos` ADD FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`);

ALTER TABLE `itens_pedido` ADD FOREIGN KEY (`id_pedido`) REFERENCES `pedidos` (`id_pedido`);

ALTER TABLE `itens_pedido` ADD FOREIGN KEY (`id_produto`) REFERENCES `produtos` (`id_produto`);
