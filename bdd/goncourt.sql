-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 08 déc. 2025 à 13:46
-- Version du serveur : 8.4.7
-- Version de PHP : 8.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `goncourt`
--

-- --------------------------------------------------------

--
-- Structure de la table `author`
--

DROP TABLE IF EXISTS `author`;
CREATE TABLE IF NOT EXISTS `author` (
  `id_author` int NOT NULL AUTO_INCREMENT,
  `id_person` int NOT NULL,
  PRIMARY KEY (`id_author`),
  KEY `id_person` (`id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `author`
--

INSERT INTO `author` (`id_author`, `id_person`) VALUES
(1, 11),
(2, 12),
(3, 13),
(4, 14),
(5, 15),
(6, 16),
(7, 17),
(8, 18),
(9, 19),
(10, 20),
(11, 21),
(12, 22),
(13, 23),
(14, 24),
(15, 25);

-- --------------------------------------------------------

--
-- Structure de la table `book`
--

DROP TABLE IF EXISTS `book`;
CREATE TABLE IF NOT EXISTS `book` (
  `id_book` int NOT NULL AUTO_INCREMENT,
  `title` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `summary` tinytext COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_author` int NOT NULL,
  `id_publisher` int NOT NULL,
  `published_date` date NOT NULL,
  `page_amount` int NOT NULL,
  `isbn` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` decimal(8,2) NOT NULL,
  PRIMARY KEY (`id_book`),
  KEY `id_author` (`id_author`),
  KEY `id_publisher` (`id_publisher`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `jury`
--

DROP TABLE IF EXISTS `jury`;
CREATE TABLE IF NOT EXISTS `jury` (
  `id_jury` int NOT NULL AUTO_INCREMENT,
  `id_book` int NOT NULL,
  `id_person` int NOT NULL,
  PRIMARY KEY (`id_jury`),
  KEY `id_book` (`id_book`),
  KEY `id_person` (`id_person`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `person`
--

DROP TABLE IF EXISTS `person`;
CREATE TABLE IF NOT EXISTS `person` (
  `id_person` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `person`
--

INSERT INTO `person` (`id_person`, `first_name`, `last_name`) VALUES
(1, 'Didier', 'Decoin'),
(2, 'Françoise', 'Chandernagor'),
(3, 'Tahar Ben', 'Jelloun'),
(4, 'Paule', 'Constant'),
(5, 'Philippe', 'Claudel'),
(6, 'Pierre', 'Assouline'),
(7, 'Eric-Emmanuel', 'Schmitt'),
(8, 'Camille', 'Laurens'),
(9, 'Pascal', 'Bruckner'),
(10, 'Christine', 'Angot'),
(11, 'Nathacha', 'Appanah'),
(12, 'Emmanuel', 'Carrère'),
(13, 'Laurent', 'Mauvignier'),
(14, 'Maria', 'Pourchet'),
(15, 'David', 'Thomas'),
(16, 'Paul', 'Gasnier'),
(17, 'Caroline', 'Lamarche'),
(18, 'David', 'Diop'),
(19, 'David', 'Deneufgermain'),
(20, 'Yanick', 'Lahens'),
(21, 'Charif', 'Majdalani'),
(22, 'Ghislaine', 'Dunant'),
(23, 'Hélène', 'Laurain'),
(24, 'Guillaume', 'Poix'),
(25, 'Alfred', 'De Montesquiou');

-- --------------------------------------------------------

--
-- Structure de la table `publisher`
--

DROP TABLE IF EXISTS `publisher`;
CREATE TABLE IF NOT EXISTS `publisher` (
  `id_publisher` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_publisher`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `publisher`
--

INSERT INTO `publisher` (`id_publisher`, `name`) VALUES
(1, 'Gallimard'),
(2, 'POL'),
(3, 'Minuit'),
(4, 'Stock'),
(5, 'Ed. de l\'Olivier'),
(6, 'Seuil'),
(7, 'Julliard'),
(8, 'Editions Marchialy'),
(9, 'Sabine Wespieser édi'),
(10, 'Albin Michel'),
(11, 'Verdier'),
(12, 'R. Laffont');

-- --------------------------------------------------------

--
-- Structure de la table `winner`
--

DROP TABLE IF EXISTS `winner`;
CREATE TABLE IF NOT EXISTS `winner` (
  `id_winner` int NOT NULL AUTO_INCREMENT,
  `published_date` date NOT NULL,
  `id_book` int NOT NULL,
  PRIMARY KEY (`id_winner`),
  KEY `id_book` (`id_book`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `author`
--
ALTER TABLE `author`
  ADD CONSTRAINT `author_fk_id` FOREIGN KEY (`id_person`) REFERENCES `person` (`id_person`);

--
-- Contraintes pour la table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `book_fk_1` FOREIGN KEY (`id_author`) REFERENCES `author` (`id_author`),
  ADD CONSTRAINT `book_fk_2` FOREIGN KEY (`id_publisher`) REFERENCES `publisher` (`id_publisher`);

--
-- Contraintes pour la table `jury`
--
ALTER TABLE `jury`
  ADD CONSTRAINT `jury_fk_1` FOREIGN KEY (`id_book`) REFERENCES `book` (`id_book`),
  ADD CONSTRAINT `jury_fk_2` FOREIGN KEY (`id_person`) REFERENCES `person` (`id_person`);

--
-- Contraintes pour la table `winner`
--
ALTER TABLE `winner`
  ADD CONSTRAINT `winner_fk_id` FOREIGN KEY (`id_book`) REFERENCES `book` (`id_book`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
