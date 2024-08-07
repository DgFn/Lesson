PGDMP  4    ,                |            post    16.2    16.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16397    post    DATABASE     x   CREATE DATABASE post WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE post;
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                pg_database_owner    false            	           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   pg_database_owner    false    4            �            1259    16516    comments    TABLE     �   CREATE TABLE public.comments (
    id integer NOT NULL,
    text character varying NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);
    DROP TABLE public.comments;
       public         heap    postgres    false    4            �            1259    16515    comments_id_seq    SEQUENCE     �   ALTER TABLE public.comments ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.comments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    4    222            �            1259    16487    likes    TABLE     s   CREATE TABLE public.likes (
    id integer NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);
    DROP TABLE public.likes;
       public         heap    postgres    false    4            �            1259    16486    likes_id_seq    SEQUENCE     �   ALTER TABLE public.likes ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.likes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    220    4            �            1259    16474    posts    TABLE     �   CREATE TABLE public.posts (
    id integer NOT NULL,
    title character varying NOT NULL,
    description character varying NOT NULL,
    user_id integer NOT NULL
);
    DROP TABLE public.posts;
       public         heap    postgres    false    4            �            1259    16473    posts_id_seq    SEQUENCE     �   ALTER TABLE public.posts ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.posts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    4    218            �            1259    16458    users    TABLE     �   CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer NOT NULL,
    gender character varying,
    nationality character varying NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false    4            �            1259    16457    users_id_seq    SEQUENCE     �   ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    216    4                      0    16516    comments 
   TABLE DATA                 public          postgres    false    222   I                   0    16487    likes 
   TABLE DATA                 public          postgres    false    220   1!       �          0    16474    posts 
   TABLE DATA                 public          postgres    false    218   �!       �          0    16458    users 
   TABLE DATA                 public          postgres    false    216   �"       
           0    0    comments_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.comments_id_seq', 5, true);
          public          postgres    false    221                       0    0    likes_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.likes_id_seq', 6, true);
          public          postgres    false    219                       0    0    posts_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.posts_id_seq', 5, true);
          public          postgres    false    217                       0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 5, true);
          public          postgres    false    215            f           2606    16522    comments comments_pk 
   CONSTRAINT     R   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pk PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_pk;
       public            postgres    false    222            d           2606    16491    likes likes_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_pk PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.likes DROP CONSTRAINT likes_pk;
       public            postgres    false    220            b           2606    16480    posts posts_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pk PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.posts DROP CONSTRAINT posts_pk;
       public            postgres    false    218            `           2606    16464    users users_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pk;
       public            postgres    false    216            j           2606    16549    comments comments_posts_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_posts_fk FOREIGN KEY (post_id) REFERENCES public.posts(id) ON UPDATE CASCADE ON DELETE CASCADE;
 D   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_posts_fk;
       public          postgres    false    222    4706    218            k           2606    16555    comments comments_users_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE CASCADE ON DELETE CASCADE;
 D   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_users_fk;
       public          postgres    false    216    4704    222            h           2606    16492    likes likes_posts_fk    FK CONSTRAINT     s   ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_posts_fk FOREIGN KEY (post_id) REFERENCES public.posts(id);
 >   ALTER TABLE ONLY public.likes DROP CONSTRAINT likes_posts_fk;
       public          postgres    false    218    220    4706            i           2606    16497    likes likes_users_fk    FK CONSTRAINT     s   ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);
 >   ALTER TABLE ONLY public.likes DROP CONSTRAINT likes_users_fk;
       public          postgres    false    220    216    4704            g           2606    16544    posts posts_users_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE CASCADE ON DELETE CASCADE;
 >   ALTER TABLE ONLY public.posts DROP CONSTRAINT posts_users_fk;
       public          postgres    false    218    216    4704               �   x���=
�@���b:����B�,h�$
�J
�?P{���"vV6�@ňĿ+�����a��e���(ǳ]���h���|2���Z�uUM9u�o7�Sm����([0)�#.�A�7q(��YPɘT�ʕ�¢�-μ%�x�n����|y�!�x���r"z���@���JI`i�!��D���e���%-�5�$�1��E	��kq���?�d          i   x���v
Q���W((M��L����N-V�s
�t��sW�q�Us�	u���
�:
@d�i��I�F:
@dH��`#�(1��cJ�0��#f���' ]$o�      �     x���=K�P�����EA�~MN�\����Z'A��v7���t,h��1~DKm���|oZQW3�����sι�� �G-���g�����/�����G���w"��q��ܡ�T����z�\��ε�)#������`�S�>��wM���D��������%ΩD�B��LG�ӘtM�6`+*ex5KS�E��܂��12;گ���=������LTZ��v�GnwIL�T����.S�2���~B��7��-�e�#��p�V���.k�8_���      �     x����j�@��y����T<	e�����WŃЃT�k{�C��
>@�F���W��:��>@�e��f��|����"�������àW���#�j{A�����Nyw�ݼ�����rA�x�A
CO�݂�TX�g$8�$�T*�w���f4�U.��+^PX!Ff1HP/���1Cbl8c��9�Ui�FZ"��-
Cy&wo�yf앴{Ł����(�Ik���i�ݿH�� �l#����	tb'Y�v�1V>�}����}# C     