CREATE DATABASE IF NOT EXISTS `tarefas`;

USE `tarefas`;

CREATE TABLE `tarefas` (
  `id_tarefa` bigint NOT NULL AUTO_INCREMENT,
  `titulo_tarefa` varchar(100) NOT NULL,
  `data_conclusao` datetime DEFAULT NULL,
  PRIMARY KEY (`id_tarefa`)
);