# Lesson 12
#БД и диаграмма
--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

-- Started on 2024-06-29 19:15:07

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 4872 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 16516)
-- Name: comments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comments (
    id integer NOT NULL,
    text character varying NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);


ALTER TABLE public.comments OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16515)
-- Name: comments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.comments ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.comments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 220 (class 1259 OID 16487)
-- Name: likes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.likes (
    id integer NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);


ALTER TABLE public.likes OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16486)
-- Name: likes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.likes ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.likes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 218 (class 1259 OID 16474)
-- Name: posts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    title character varying NOT NULL,
    description character varying NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.posts OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16473)
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.posts ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.posts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 216 (class 1259 OID 16458)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer NOT NULL,
    gender character varying,
    nationality character varying NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16457)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4866 (class 0 OID 16516)
-- Dependencies: 222
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (1, 'Зачем тебе else?', 2, 2);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (2, 'Ты прав, полностью поддерживаю', 3, 3);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (3, 'А как иначе?', 1, 1);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (5, 'Ну Никитос', 3, 1);


--
-- TOC entry 4864 (class 0 OID 16487)
-- Dependencies: 220
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (1, 1, 5);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (2, 2, 1);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (3, 2, 2);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (4, 1, 3);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (5, 2, 1);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (6, 5, 5);


--
-- TOC entry 4862 (class 0 OID 16474)
-- Dependencies: 218
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (1, 'Менторю', 'Сегодня менторил джуника', 2);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (2, 'Шкила', 'Учился у ментора', 1);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (3, 'Девушки', 'Все девушки зло', 3);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (4, 'Улица', 'Покуса бабку', 4);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (5, 'Раша', 'Раша лучше чем наша', 5);


--
-- TOC entry 4860 (class 0 OID 16458)
-- Dependencies: 216
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (1, 'Никита', 22, 'человеческий', 'Русский');
INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (2, 'Санечек', 80, 'красавчик', 'Русский');
INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (3, 'Дрюня', 23, 'рептилоид', 'Русский');
INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (4, 'Альма', 2, 'пес', 'Француз');
INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (5, 'Джон', 15, 'пельмень', 'Американец');


--
-- TOC entry 4873 (class 0 OID 0)
-- Dependencies: 221
-- Name: comments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.comments_id_seq', 5, true);


--
-- TOC entry 4874 (class 0 OID 0)
-- Dependencies: 219
-- Name: likes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.likes_id_seq', 6, true);


--
-- TOC entry 4875 (class 0 OID 0)
-- Dependencies: 217
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.posts_id_seq', 5, true);


--
-- TOC entry 4876 (class 0 OID 0)
-- Dependencies: 215
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 5, true);


--
-- TOC entry 4710 (class 2606 OID 16522)
-- Name: comments comments_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pk PRIMARY KEY (id);


--
-- TOC entry 4708 (class 2606 OID 16491)
-- Name: likes likes_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_pk PRIMARY KEY (id);


--
-- TOC entry 4706 (class 2606 OID 16480)
-- Name: posts posts_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pk PRIMARY KEY (id);


--
-- TOC entry 4704 (class 2606 OID 16464)
-- Name: users users_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);


--
-- TOC entry 4714 (class 2606 OID 16549)
-- Name: comments comments_posts_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_posts_fk FOREIGN KEY (post_id) REFERENCES public.posts(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 4715 (class 2606 OID 16555)
-- Name: comments comments_users_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 4712 (class 2606 OID 16492)
-- Name: likes likes_posts_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_posts_fk FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- TOC entry 4713 (class 2606 OID 16497)
-- Name: likes likes_users_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- TOC entry 4711 (class 2606 OID 16544)
-- Name: posts posts_users_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2024-06-29 19:15:08

--
-- PostgreSQL database dump complete
--



![db1.sql](post%20-%20public%20-%20posts.png)
