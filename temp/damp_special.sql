PGDMP                     
    y            traffic_analyzer    13.2    13.2     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    59515    traffic_analyzer    DATABASE     m   CREATE DATABASE traffic_analyzer WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
     DROP DATABASE traffic_analyzer;
                postgres    false            ?            1259    59518    frame    TABLE     6  CREATE TABLE public.frame (
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
    DROP TABLE public.frame;
       public         heap    postgres    false            ?            1259    59516    frame_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.frame_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.frame_id_seq;
       public          postgres    false    201            ?           0    0    frame_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.frame_id_seq OWNED BY public.frame.id;
          public          postgres    false    200            ?            1259    59529    ip_location    TABLE        CREATE TABLE public.ip_location (
    id integer NOT NULL,
    ip inet,
    country character varying(100),
    country_code character varying(5),
    latitude real,
    longitude real,
    region character varying(100),
    city character varying(100)
);
    DROP TABLE public.ip_location;
       public         heap    postgres    false            ?            1259    59527    ip_location_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.ip_location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.ip_location_id_seq;
       public          postgres    false    203            ?           0    0    ip_location_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.ip_location_id_seq OWNED BY public.ip_location.id;
          public          postgres    false    202            *           2604    59521    frame id    DEFAULT     d   ALTER TABLE ONLY public.frame ALTER COLUMN id SET DEFAULT nextval('public.frame_id_seq'::regclass);
 7   ALTER TABLE public.frame ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    200    201    201            +           2604    59532    ip_location id    DEFAULT     p   ALTER TABLE ONLY public.ip_location ALTER COLUMN id SET DEFAULT nextval('public.ip_location_id_seq'::regclass);
 =   ALTER TABLE public.ip_location ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203            ?          0    59518    frame 
   TABLE DATA           z   COPY public.frame (id, protocol, s_mac, d_mac, s_ip, d_ip, s_port, d_port, data, arrival_time, delivery_time) FROM stdin;
    public          postgres    false    201   B       ?          0    59529    ip_location 
   TABLE DATA           g   COPY public.ip_location (id, ip, country, country_code, latitude, longitude, region, city) FROM stdin;
    public          postgres    false    203   _       ?           0    0    frame_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.frame_id_seq', 1, false);
          public          postgres    false    200            ?           0    0    ip_location_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.ip_location_id_seq', 1, false);
          public          postgres    false    202            -           2606    59526    frame frame_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.frame
    ADD CONSTRAINT frame_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.frame DROP CONSTRAINT frame_pkey;
       public            postgres    false    201            /           2606    59537    ip_location ip_location_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.ip_location
    ADD CONSTRAINT ip_location_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.ip_location DROP CONSTRAINT ip_location_pkey;
       public            postgres    false    203            1           2606    59543    frame frame_d_ip_fkey    FK CONSTRAINT     w   ALTER TABLE ONLY public.frame
    ADD CONSTRAINT frame_d_ip_fkey FOREIGN KEY (d_ip) REFERENCES public.ip_location(id);
 ?   ALTER TABLE ONLY public.frame DROP CONSTRAINT frame_d_ip_fkey;
       public          postgres    false    2863    201    203            0           2606    59538    frame frame_s_ip_fkey    FK CONSTRAINT     w   ALTER TABLE ONLY public.frame
    ADD CONSTRAINT frame_s_ip_fkey FOREIGN KEY (s_ip) REFERENCES public.ip_location(id);
 ?   ALTER TABLE ONLY public.frame DROP CONSTRAINT frame_s_ip_fkey;
       public          postgres    false    203    201    2863            ?      x?????? ? ?      ?      x?????? ? ?     