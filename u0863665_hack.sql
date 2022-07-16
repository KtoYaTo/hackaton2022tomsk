-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Июл 16 2022 г., 06:27
-- Версия сервера: 5.7.27-30
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `u0863665_hack`
--

-- --------------------------------------------------------

--
-- Структура таблицы `dataset`
--

CREATE TABLE `dataset` (
  `id` int(11) NOT NULL,
  `productNumber` int(11) DEFAULT NULL,
  `techReg` text,
  `productGroup` text,
  `generalProductName` text,
  `il` varchar(255) DEFAULT NULL,
  `applicant` varchar(255) DEFAULT NULL,
  `applicantAddress` varchar(255) DEFAULT NULL,
  `manufacturer` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `manufacturerAddress` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Структура таблицы `tndv_codes`
--

CREATE TABLE `tndv_codes` (
  `id` int(11) NOT NULL,
  `code` int(11) NOT NULL,
  `dataset_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `dataset`
--
ALTER TABLE `dataset`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `tndv_codes`
--
ALTER TABLE `tndv_codes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `dataset`
--
ALTER TABLE `dataset`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=337;

--
-- AUTO_INCREMENT для таблицы `tndv_codes`
--
ALTER TABLE `tndv_codes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=384;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
