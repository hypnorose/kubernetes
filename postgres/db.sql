-- Table: public.numbers

-- DROP TABLE public.numbers;
CREATE DATABASE db;
CREATE TABLE IF NOT EXISTS public.numbers
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    value bigint,
    CONSTRAINT numbers_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.numbers
    OWNER to postgres;