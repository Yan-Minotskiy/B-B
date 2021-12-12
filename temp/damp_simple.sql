--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-11-13 16:24:35

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 201 (class 1259 OID 59518)
-- Name: frame; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.frame (
    id integer NOT NULL,
    protocol character varying(10),
    s_mac macaddr,
    d_mac macaddr,
    s_ip integer,
    d_ip integer,
    s_port smallint,
    d_port smallint,
    data text,
    arrival_time timestamp without time zone,
    delivery_time time without time zone
);


ALTER TABLE public.frame OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 59516)
-- Name: frame_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.frame_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.frame_id_seq OWNER TO postgres;

--
-- TOC entry 3005 (class 0 OID 0)
-- Dependencies: 200
-- Name: frame_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.frame_id_seq OWNED BY public.frame.id;


--
-- TOC entry 203 (class 1259 OID 59529)
-- Name: ip_location; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ip_location (
    id integer NOT NULL,
    ip inet,
    country character varying(100),
    country_code character varying(5),
    latitude real,
    longitude real,
    region character varying(100),
    city character varying(100)
);


ALTER TABLE public.ip_location OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 59527)
-- Name: ip_location_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ip_location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ip_location_id_seq OWNER TO postgres;

--
-- TOC entry 3006 (class 0 OID 0)
-- Dependencies: 202
-- Name: ip_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ip_location_id_seq OWNED BY public.ip_location.id;


--
-- TOC entry 2858 (class 2604 OID 59521)
-- Name: frame id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.frame ALTER COLUMN id SET DEFAULT nextval('public.frame_id_seq'::regclass);


--
-- TOC entry 2859 (class 2604 OID 59532)
-- Name: ip_location id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ip_location ALTER COLUMN id SET DEFAULT nextval('public.ip_location_id_seq'::regclass);


--
-- TOC entry 2997 (class 0 OID 59518)
-- Dependencies: 201
-- Data for Name: frame; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2999 (class 0 OID 59529)
-- Dependencies: 203
-- Data for Name: ip_location; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3007 (class 0 OID 0)
-- Dependencies: 200
-- Name: frame_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.frame_id_seq', 1, false);


--
-- TOC entry 3008 (class 0 OID 0)
-- Dependencies: 202
-- Name: ip_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ip_location_id_seq', 1, false);


--
-- TOC entry 2861 (class 2606 OID 59526)
-- Name: frame frame_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.frame
    ADD CONSTRAINT frame_pkey PRIMARY KEY (id);


--
-- TOC entry 2863 (class 2606 OID 59537)
-- Name: ip_location ip_location_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ip_location
    ADD CONSTRAINT ip_location_pkey PRIMARY KEY (id);


--
-- TOC entry 2865 (class 2606 OID 59543)
-- Name: frame frame_d_ip_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.frame
    ADD CONSTRAINT frame_d_ip_fkey FOREIGN KEY (d_ip) REFERENCES public.ip_location(id);


--
-- TOC entry 2864 (class 2606 OID 59538)
-- Name: frame frame_s_ip_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.frame
    ADD CONSTRAINT frame_s_ip_fkey FOREIGN KEY (s_ip) REFERENCES public.ip_location(id);


-- Completed on 2021-11-13 16:24:35

--
-- PostgreSQL database dump complete
--

