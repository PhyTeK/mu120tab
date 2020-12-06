--
-- PostgreSQL database dump
--

-- Dumped from database version 11.9 (Debian 11.9-0+deb10u1)
-- Dumped by pg_dump version 11.9 (Debian 11.9-0+deb10u1)

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

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO phimar;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: phimar
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO phimar;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: phimar
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO phimar;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: phimar
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO phimar;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: phimar
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO phimar;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: phimar
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO phimar;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: phimar
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO phimar;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO phimar;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: phimar
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO phimar;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: phimar
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: phimar
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO phimar;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: phimar
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO phimar;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: phimar
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO phimar;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: phimar
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO phimar;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: phimar
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO phimar;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: phimar
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO phimar;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: phimar
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO phimar;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: phimar
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO phimar;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: phimar
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO phimar;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: phimar
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO phimar;

--
-- Name: mu_multi; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.mu_multi (
    testid integer NOT NULL,
    week smallint,
    date character varying(80),
    start character varying(80),
    "end" character varying(80),
    tid character varying(80),
    correct integer,
    errors integer,
    "1: 6x6" character varying(4),
    "2: 8x4" character varying(4),
    "3: 6x3" character varying(4),
    "4: 2x2" character varying(4),
    "5: 5x9" character varying(4),
    "6: 7x5" character varying(4),
    "7: 3x7" character varying(4),
    "8: 9x9" character varying(4),
    "9: 8x6" character varying(4),
    "10: 6x7" character varying(4),
    "11: 3x8" character varying(4),
    "12: 9x4" character varying(4),
    "13: 4x8" character varying(4),
    "14: 6x4" character varying(4),
    "15: 7x7" character varying(4),
    "16: 9x3" character varying(4),
    "17: 4x6" character varying(4),
    "18: 6x8" character varying(4),
    "19: 3x9" character varying(4),
    "20: 8x8" character varying(4),
    "21: 9x6" character varying(4),
    "22: 4x7" character varying(4),
    "23: 5x8" character varying(4),
    "24: 8x3" character varying(4),
    "25: 6x9" character varying(4),
    "26: 7x3" character varying(4),
    "27: 4x9" character varying(4),
    "28: 3x6" character varying(4),
    "29: 7x4" character varying(4),
    "30: 10x10" character varying(4),
    "31: 7x7" character varying(4),
    "32: 8x6" character varying(4),
    "33: 1x5" character varying(4),
    "34: 8x8" character varying(4),
    "35: 6x9" character varying(4),
    "36: 0x7" character varying(4),
    "37: 5x3" character varying(4),
    "38: 9x9" character varying(4),
    "39: 8x7" character varying(4),
    "40: 7x3" character varying(4),
    "41: 3x2" character varying(4),
    "42: 4x8" character varying(4),
    "43: 6x7" character varying(4),
    "44: 8x7" character varying(4),
    "45: 7x3" character varying(4),
    "46: 3x2" character varying(4),
    "47: 4x8" character varying(4),
    "48: 9x7" character varying(4),
    "49: 3x8" character varying(4),
    "50: 4x7" character varying(4),
    "51: 6x8" character varying(4),
    "52: 3x6" character varying(4),
    "53: 5x9" character varying(4),
    "54: 4x6" character varying(4),
    "55: 9x6" character varying(4),
    "56: 3x0" character varying(4),
    "57: 7x6" character varying(4),
    "58: 8x4" character varying(4),
    "59: 3x7" character varying(4),
    "60: 5x5" character varying(4),
    "61: 6x0" character varying(4),
    "62: 7x6" character varying(4),
    "63: 1x1" character varying(4),
    "64: 4x6" character varying(4),
    "65: 8x7" character varying(4),
    "66: 7x3" character varying(4),
    "67: 9x9" character varying(4),
    "68: 8x6" character varying(4),
    "69: 6x3" character varying(4),
    "70: 6x9" character varying(4),
    "71: 8x8" character varying(4),
    "72: 9x6" character varying(4),
    "73: 7x4" character varying(4),
    "74: 3x8" character varying(4),
    "75: 7x9" character varying(4),
    "76: 6x5" character varying(4),
    "77: 9x8" character varying(4),
    "78: 6x6" character varying(4),
    "79: 8x9" character varying(4),
    "80: 6x7" character varying(4),
    "81: 2x4" character varying(4),
    "82: 9x4" character varying(4),
    "83: 7x7" character varying(4),
    "84: 4x8" character varying(4),
    "85: 3x9" character varying(4),
    "86: 7x8" character varying(4),
    "87: 6x8" character varying(4),
    "88: 9x7" character varying(4),
    "89: 1x4" character varying(4),
    "90: 9x2" character varying(4),
    "91: 7x4" character varying(4),
    "92: 9x6" character varying(4),
    "93: 7x8" character varying(4),
    "94: 9x9" character varying(4),
    "95: 7x6" character varying(4),
    "96: 8x3" character varying(4),
    "97: 6x6" character varying(4),
    "98: 4x9" character varying(4),
    "99: 8x8" character varying(4),
    "100: 4x7" character varying(4),
    "101: 9x3" character varying(4),
    "102: 7x7" character varying(4),
    "103: 7x9" character varying(4),
    "104: 4x6" character varying(4),
    "105: 8x4" character varying(4),
    "106: 9x7" character varying(4),
    "107: 8x6" character varying(4),
    "108: 7x3" character varying(4),
    "109: 6x4" character varying(4),
    "110: 9x8" character varying(4),
    "111: 6x7" character varying(4),
    "112: 8x9" character varying(4),
    "113: 3x7" character varying(4),
    "114: 6x9" character varying(4),
    "115: 6x8" character varying(4),
    "116: 2x0" character varying(4),
    "117: 8x7" character varying(4),
    "118: 6x3" character varying(4),
    "119: 7x2" character varying(4),
    "120: 10x1" character varying(4),
    studid_id integer NOT NULL,
    CONSTRAINT mu_multi_week_check CHECK ((week >= 0))
);


ALTER TABLE public.mu_multi OWNER TO phimar;

--
-- Name: mu_multi_testid_seq; Type: SEQUENCE; Schema: public; Owner: phimar
--

CREATE SEQUENCE public.mu_multi_testid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mu_multi_testid_seq OWNER TO phimar;

--
-- Name: mu_multi_testid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: phimar
--

ALTER SEQUENCE public.mu_multi_testid_seq OWNED BY public.mu_multi.testid;


--
-- Name: mu_results; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.mu_results (
    id integer NOT NULL,
    klasser character varying(2) NOT NULL,
    name character varying(20) NOT NULL,
    test character varying(2) NOT NULL
);


ALTER TABLE public.mu_results OWNER TO phimar;

--
-- Name: mu_results_id_seq; Type: SEQUENCE; Schema: public; Owner: phimar
--

CREATE SEQUENCE public.mu_results_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mu_results_id_seq OWNER TO phimar;

--
-- Name: mu_results_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: phimar
--

ALTER SEQUENCE public.mu_results_id_seq OWNED BY public.mu_results.id;


--
-- Name: mu_stud; Type: TABLE; Schema: public; Owner: phimar
--

CREATE TABLE public.mu_stud (
    studid integer NOT NULL,
    name character varying(80) NOT NULL,
    fname character varying(80),
    klass character varying(8) NOT NULL
);


ALTER TABLE public.mu_stud OWNER TO phimar;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: mu_multi testid; Type: DEFAULT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.mu_multi ALTER COLUMN testid SET DEFAULT nextval('public.mu_multi_testid_seq'::regclass);


--
-- Name: mu_results id; Type: DEFAULT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.mu_results ALTER COLUMN id SET DEFAULT nextval('public.mu_results_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add stud	7	add_stud
26	Can change stud	7	change_stud
27	Can delete stud	7	delete_stud
28	Can view stud	7	view_stud
29	Can add multi	8	add_multi
30	Can change multi	8	change_multi
31	Can delete multi	8	delete_multi
32	Can view multi	8	view_multi
33	Can add results	9	add_results
34	Can change results	9	change_results
35	Can delete results	9	delete_results
36	Can view results	9	view_results
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$216000$b1GzG4i03RXp$e7l/lgqU0Euo6Xsf1QoPbNS3GT+j+dNRHQO75Ss4Taw=	2020-12-01 09:11:21.345389+00	t	phimar			phi.mar.email@gmail.com	t	t	2020-11-28 21:20:10.084882+00
2	pbkdf2_sha256$216000$ki3XFKG0o78H$67XaAZqHmu0r/90mvXX9KYCjn6X1+1H7H5qNdOHJaXg=	\N	f	Tatyana				f	t	2020-11-28 21:55:34.275584+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2020-11-28 21:55:34.432389+00	2	Tatyana	1	[{"added": {}}]	4	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	mu	stud
8	mu	multi
9	mu	results
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2020-11-28 19:40:22.052559+00
2	auth	0001_initial	2020-11-28 19:40:22.300863+00
3	admin	0001_initial	2020-11-28 19:40:22.591758+00
4	admin	0002_logentry_remove_auto_add	2020-11-28 19:40:22.647352+00
5	admin	0003_logentry_add_action_flag_choices	2020-11-28 19:40:22.661534+00
6	contenttypes	0002_remove_content_type_name	2020-11-28 19:40:22.688976+00
7	auth	0002_alter_permission_name_max_length	2020-11-28 19:40:22.705758+00
8	auth	0003_alter_user_email_max_length	2020-11-28 19:40:22.720194+00
9	auth	0004_alter_user_username_opts	2020-11-28 19:40:22.734982+00
10	auth	0005_alter_user_last_login_null	2020-11-28 19:40:22.749093+00
11	auth	0006_require_contenttypes_0002	2020-11-28 19:40:22.754792+00
12	auth	0007_alter_validators_add_error_messages	2020-11-28 19:40:22.77118+00
13	auth	0008_alter_user_username_max_length	2020-11-28 19:40:22.816587+00
14	auth	0009_alter_user_last_name_max_length	2020-11-28 19:40:22.84406+00
15	auth	0010_alter_group_name_max_length	2020-11-28 19:40:22.860679+00
16	auth	0011_update_proxy_permissions	2020-11-28 19:40:22.876232+00
17	auth	0012_alter_user_first_name_max_length	2020-11-28 19:40:22.889358+00
18	mu	0001_initial	2020-11-28 19:40:22.97708+00
19	mu	0002_auto_20201127_1102	2020-11-28 19:40:23.032861+00
20	mu	0003_auto_20201127_1112	2020-11-28 19:40:23.054471+00
21	mu	0004_auto_20201127_1207	2020-11-28 19:40:23.079219+00
22	mu	0005_auto_20201127_1558	2020-11-28 19:40:23.189483+00
23	mu	0006_auto_20201127_1600	2020-11-28 19:40:23.215844+00
24	mu	0007_auto_20201127_1627	2020-11-28 19:40:23.394839+00
25	mu	0008_auto_20201127_1628	2020-11-28 19:40:23.44082+00
26	mu	0009_auto_20201127_1638	2020-11-28 19:40:23.464127+00
27	mu	0010_auto_20201127_1708	2020-11-28 19:40:23.520057+00
28	mu	0011_auto_20201127_1826	2020-11-28 19:40:23.592579+00
29	mu	0012_auto_20201127_1859	2020-11-28 19:40:23.706988+00
30	mu	0013_auto_20201127_1924	2020-11-28 19:40:23.785342+00
31	mu	0014_auto_20201127_1935	2020-11-28 19:40:23.833599+00
32	mu	0015_auto_20201127_1937	2020-11-28 19:40:23.847945+00
33	mu	0016_auto_20201127_1942	2020-11-28 19:40:23.886283+00
34	mu	0017_auto_20201127_2019	2020-11-28 19:40:23.902732+00
35	sessions	0001_initial	2020-11-28 19:40:23.94369+00
36	mu	0018_results	2020-11-30 19:00:13.25149+00
37	mu	0019_auto_20201201_1513	2020-12-01 14:13:11.146691+00
38	mu	0020_auto_20201201_1803	2020-12-01 17:03:57.841331+00
39	mu	0021_auto_20201201_2246	2020-12-01 21:46:31.93481+00
40	mu	0022_auto_20201203_2147	2020-12-06 15:25:54.265886+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
uaxwzgwjhsrnhts4q2v707yrmaingzwv	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj7eA:pcjZRLy48g5ALu79J3Try0-exImcS0UNQJdk4JWgp7k	2020-12-12 21:20:46.296066+00
db752y7x1s02ic9clbboggu2p3p4ckkk	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj7f7:PELX7yJu7xRznQWRbfQaJtO8C8rgw2l5JvYeRvlOGKw	2020-12-12 21:21:45.982654+00
fcmb0micuoat6wg5mwnk9q1h5yfdz8sa	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj7l3:zHU1oTLkT_vEu-F77v7uNiOQTjIwJMVLTrCGUv5RkwE	2020-12-12 21:27:53.598566+00
vb8m3348kt6h6w9x13p8foguwfnrj9dq	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj7vF:ULYnNXYeWWbIC5hH373tX0KpsCfVMOl2wWv67vMdnCY	2020-12-12 21:38:25.308847+00
b1tmlgxwwgf642bk9nlbm4ld4zvlsddm	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj7vZ:d68QMTzhbxSGVTXhvG2uxe021DS1qMgz3DMC3SobSow	2020-12-12 21:38:45.330828+00
v4x8toxa2alzxf4plv90lxo8xhm4uwli	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj7vx:XGRI-ny_o0tCNnM_ti0K04N6eUsBhgUlE5UvihiHuzA	2020-12-12 21:39:09.338947+00
r9rpbuu7avzn2baqlvieqso4thwn8wd4	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj7xt:JUVCe42-_GdPxrlKNgK1MS-xo_9mGrORrjuLE8UYZ4E	2020-12-12 21:41:09.180517+00
n0ukf06lxzk2ddnqej07noo0ioiegu2r	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj7yH:Yw1Z8_iqCR36hw60oyDVXUaE6aFLZ1WAAUiv6vsWek8	2020-12-12 21:41:33.872239+00
wackj0f2ivxodw8g3wo2ul12xe5gt151	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj7yk:V4JEBDwzhyryfl82A3boVT3hnTr-5DxogKsjKk-J4_A	2020-12-12 21:42:02.679868+00
4o40xa6z8xmo88muomzmxojcs3r5bsqn	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj81m:LsQ9WdxsU4ioN2lwMUsV0xmYoZR3vHbakSfOS4zhde4	2020-12-12 21:45:10.807278+00
ot8dvt8034awyr9lw6inpt74dl2pyud6	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj823:T0mKKvjzfT-AI8imwMK9cZbmxLaDhMLbr-zphpEwVZw	2020-12-12 21:45:27.224309+00
0cfwy46kbaonnhi38nyifiqbpy05jhux	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj833:fP-BvX6pPp8PmmhW_upyCRmRcsxinGzHxg5VJhuB3Tk	2020-12-12 21:46:29.919372+00
1a2cihjaxgk4u5geug2c4xkjv5n8q06q	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj83A:qRiXIXhUpPC7FiSMlRWmAui1zXAny95DK0HGy4afddQ	2020-12-12 21:46:36.953209+00
86xjgl3zyci0uc6dl5rrpvhrrg23nw6i	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj85K:8ojMSgSCyjguuSUBjEoT8md1xJ5-7J6sh3eofCr_wu0	2020-12-12 21:48:50.478729+00
26fsagjz59rldfy65n6mzwcz16pe5a3a	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj87h:IS4AYLm4MDrJdvMci2_JgUonWvZ7jpGKsff0BFzf48E	2020-12-12 21:51:17.775662+00
53uottt2vmb2nntgxng2ufivwzm06mk4	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj88K:REpa_8k3S06R8oMyicQhr3CsNegzRaQALWw7V5HgExA	2020-12-12 21:51:56.774015+00
k0umlbigec5zc4ogksdoq1tkf9c66yj5	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj897:ABd-hIvBiZnkWxLm2D5yPlDLQySA4kKuoWvtEAVvfKY	2020-12-12 21:52:45.478923+00
byeyk6sn7tsu32mrtdj2omllvhx05ksd	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8Ah:349EYySMuD-lD1NgxfUSmZOFsPOZEqeJ324uh88zgkw	2020-12-12 21:54:23.03495+00
26rsv2mhrlyjdw991ih8dfqpcyxd6vsz	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8Fv:lGeioQ7_RaHma-R_lqSRj-VHW52DAZbaCyMPyM-lPp0	2020-12-12 21:59:47.365796+00
gzj6bm9pw46t2vob3kp55kqs8a84f4rp	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8G4:H0N_3Ve3yFlX0LlqJU7BflRtwidvE_ly8YmEbpZy53w	2020-12-12 21:59:56.972616+00
mapogg3dpis92tksygb1fhz8btt74m7l	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8I2:e9918cvmJz-Xd9sha3V-ZnHA56faI8cozQymQPBaISM	2020-12-12 22:01:58.368225+00
4nhk1rob38qvkyk7aslo9g7r6jqq6m5i	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8Jq:JUZqufhSRvnIca_tidskAj9G2G8OTfMfmMJ7caTER4Y	2020-12-12 22:03:50.661945+00
vp5jk4939670l9lna2tj4vmzc9rgdhjg	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8K5:Jfg75JzktmJr8KtzOEi4B_EzKKZXWY_UdUhGHigAKXY	2020-12-12 22:04:05.851478+00
a2hevolsphhx8ma0qplnlabkuyf8tydj	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8KS:ImNdxiQ6ETgp3M7eInjKx1YSmf2udNLyGvSmDuLBBeo	2020-12-12 22:04:28.2354+00
o0vf5c2m2ltx83km9zglty523kfmfa2g	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8LP:f2tKnakENw4zMs5H9H42nPK1aQ04w3CGUs_4GqxcBvg	2020-12-12 22:05:27.358828+00
m06a76q3gax1xtgmu06bkgel2lo1ya0i	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8LV:n7EnOdvfFNRweq4HaYPJ9fwXQdISmrAGqtJK7ttf5v0	2020-12-12 22:05:33.512879+00
4m9c8wdp82mplj8hq6zntnmw8z7h30b9	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8M9:G4Zp7ayI3o9mQktc25gTzSQ81zXgBCivIUaDRkKKSps	2020-12-12 22:06:13.483274+00
djqqwr2imp2dc4rnjdr92qw93g5om3pp	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8Mx:DXAxdAfUYBbUNdeNH4iLmM23TwySW7rPj0jWMtZI8Og	2020-12-12 22:07:03.034218+00
1pga8v0fxyvi9l7wn88okrwbrxp3lqh1	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8Nd:stSEIhbZzjK_oHLRriASpd2U-AP-6i7mS0IUyg_aMVA	2020-12-12 22:07:45.609909+00
km6kf9eskbzj76gl41zotz0ncqn8dahm	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8QY:rAbN_w4EIHAzS0Oc0aXGC5RknEro-nEj2cP6sE7lzzw	2020-12-12 22:10:46.286425+00
8lydl80zfpjbhqfgtwfa08nrcc1nf65u	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8aH:SNwfMQMJUmrPYuRa6d_Ijoz-o3z_KVIHIVDYgRUT-p0	2020-12-12 22:20:49.108255+00
bp19x57lquj6asjrrtu6l13wzwt02vs4	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8mo:qV09O-w7w1N8ui9WaKijpclz2B_BtjMGlc8AwU8P4g8	2020-12-12 22:33:46.918296+00
u6qgks007hh8cs020x6m8nuaw0ij3qer	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8o6:m1CvcP7mKJiWhCwW7-177zCqg2WG6_Hy-B6HhzNOPCQ	2020-12-12 22:35:06.120858+00
fknf2j1r54v1x2t96kop6cm67bde8knr	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8oF:mitePRjS7VcduhZaK-mNjUifVgrS2IRN7yY5M32YzBE	2020-12-12 22:35:15.483037+00
fo2qjhh5u68ffhr7nh0o3vr8pabh9kng	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8of:BH5F-a84J2Zh8BswQDjo3E16K5VD0Q7Cd80-lVRmgt0	2020-12-12 22:35:41.507489+00
19ejoy92ibugz9hgz3f0r7hf8el6qrls	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8ow:2NAR1wWnc4zbch_Iqo_MuAaWF2xFKEjrXs1Bcu4BsdA	2020-12-12 22:35:58.935968+00
2qlzosp8xqlv7xdz3325vjntsshezgsv	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kj8pk:oWhQPETs_kmridWk099WikMor-H9aM6uYEit2q26xjw	2020-12-12 22:36:48.195016+00
6ml67vjicdzdyl78wes4hx0dmqsj63q0	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kjOHB:i2GUBAx0Aym0Y_pc8f7Th5F2tQ1aevn7-1w5JywOU2I	2020-12-13 15:06:09.366469+00
ypqdj2c6yz54y0tj75i3lvm0onhgc2m5	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kjkoM:NUB9yNveK6XAOFCsoaw9nQfYUAab21xYUmT_Ie5FeQc	2020-12-14 15:09:54.506447+00
tbtczka39ftsodbfzmxu5rthg1ibrk0c	.eJxVjEEOwiAQRe_C2hCgOAWX7nsGMswMUjVtUtqV8e7apAvd_vfef6mE21rT1mRJI6uLsur0u2Wkh0w74DtOt1nTPK3LmPWu6IM2Pcwsz-vh_h1UbPVbIxCB41yEmSB4MQASyAffGXGBI5jSW3axgC2EIWKmEsH2fLbIvlPvDwqWOKQ:1kk1gv:QtfPpap-7API36qHbOBW_5MvmCpm-83VFuFKUSzBGFk	2020-12-15 09:11:21.360062+00
\.


--
-- Data for Name: mu_multi; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.mu_multi (testid, week, date, start, "end", tid, correct, errors, "1: 6x6", "2: 8x4", "3: 6x3", "4: 2x2", "5: 5x9", "6: 7x5", "7: 3x7", "8: 9x9", "9: 8x6", "10: 6x7", "11: 3x8", "12: 9x4", "13: 4x8", "14: 6x4", "15: 7x7", "16: 9x3", "17: 4x6", "18: 6x8", "19: 3x9", "20: 8x8", "21: 9x6", "22: 4x7", "23: 5x8", "24: 8x3", "25: 6x9", "26: 7x3", "27: 4x9", "28: 3x6", "29: 7x4", "30: 10x10", "31: 7x7", "32: 8x6", "33: 1x5", "34: 8x8", "35: 6x9", "36: 0x7", "37: 5x3", "38: 9x9", "39: 8x7", "40: 7x3", "41: 3x2", "42: 4x8", "43: 6x7", "44: 8x7", "45: 7x3", "46: 3x2", "47: 4x8", "48: 9x7", "49: 3x8", "50: 4x7", "51: 6x8", "52: 3x6", "53: 5x9", "54: 4x6", "55: 9x6", "56: 3x0", "57: 7x6", "58: 8x4", "59: 3x7", "60: 5x5", "61: 6x0", "62: 7x6", "63: 1x1", "64: 4x6", "65: 8x7", "66: 7x3", "67: 9x9", "68: 8x6", "69: 6x3", "70: 6x9", "71: 8x8", "72: 9x6", "73: 7x4", "74: 3x8", "75: 7x9", "76: 6x5", "77: 9x8", "78: 6x6", "79: 8x9", "80: 6x7", "81: 2x4", "82: 9x4", "83: 7x7", "84: 4x8", "85: 3x9", "86: 7x8", "87: 6x8", "88: 9x7", "89: 1x4", "90: 9x2", "91: 7x4", "92: 9x6", "93: 7x8", "94: 9x9", "95: 7x6", "96: 8x3", "97: 6x6", "98: 4x9", "99: 8x8", "100: 4x7", "101: 9x3", "102: 7x7", "103: 7x9", "104: 4x6", "105: 8x4", "106: 9x7", "107: 8x6", "108: 7x3", "109: 6x4", "110: 9x8", "111: 6x7", "112: 8x9", "113: 3x7", "114: 6x9", "115: 6x8", "116: 2x0", "117: 8x7", "118: 6x3", "119: 7x2", "120: 10x1", studid_id) FROM stdin;
1	48	2020-11-28	21:13:58	21:14:12	0:14	1	2								!34																							!23																																																																								63																		901
2	48	2020-11-28	21:13:58	21:20:19	6:21	1	2								!34																							!23																																																																								63																		901
3	48	2020-11-28	21:20:42	21:21:24	0:42	9	3			18	4	!23	35	21													64	54	28																					!87													!65																										36	49																																						101
4	48	2020-11-28	22:08:06	22:08:11	0:5	0	0																																																																																																																									100
5	48	2020-11-28	22:10:10	22:10:14	0:4	0	0																																																																																																																									100
6	48	2020-11-28	22:27:28	22:27:34	0:6	0	0																																																																																																																									100
7	48	2020-11-28	22:41:48	22:41:52	0:4	0	0																																																																																																																									100
8	48	2020-11-28	22:48:26	22:48:33	0:7	0	0																																																																																																																									100
9	48	2020-11-28	22:58:35	22:58:48	0:13	1	2																												18																																		!23																								!5																																			200
10	48	2020-11-29	13:43:52	13:44:22	0:30	2	2	36																																																																																		!23												!12																									10	100
11	48	2020-11-29	13:43:52	13:45:17	1:25	2	2	36																																																																																		!23												!12																									10	100
\.


--
-- Data for Name: mu_results; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.mu_results (id, klasser, name, test) FROM stdin;
1	1a	You	a
2	4a	Me	a
3	3a	Me	a
4	3a	Me	a
5	3a	Me	a
6	3a	Me	a
7	3a	Me	a
8	9a	hi	a
9	1a	You	a
10	1a	hi	a
11	1a	Me	a
12	3a	hi	a
13	5a	hi	a
14	3a	hi	a
15	2a	hi	a
16	1a	hi	a
17	4a	hi	a
18	1a	hi	a
19	3a	hi	a
20	1a	hi	a
21	4a	hi	a
22	1a	hi	a
23	1a	hi	a
24	1a	Me	a
25	1a	hi	a
26	1a	hi	a
27	1a	hi	a
28	1a	hi	a
29	2a	hi	a
30	9a	hi	a
31	9b	hi	a
32	1a	hi	a
33	1a	hi	a
34	9b	hi	a
35	1a	hi	a
36	1a	hi	a
37	1a	hi	a
38	1a	hi	a
39	1a	hi	a
40	1a	hi	a
41	9b	hi	a
42	1a	hi	a
43	9b	hi	a
44	1a	hi	a
45	1a	hi	a
46	1a	hi	a
47	9b	hi	a
48	1a	hi	a
49	1a	hi	a
50	1a	hi	a
51	9b	hi	a
52	1a	hi	a
53	1a	hi	a
54	1a	hi	a
55	1a	hi	a
56	9b	hi	a
57	1a	Me	a
58	1a	Me	a
59	1a	Me	a
60	1a	Me	a
61	1a	Me	a
62	1a	Me	a
63	1a	Me	a
64	9b	Me	a
65	1a	Me	a
66	9b	Me	a
67	1a	Me	a
68	1a	Me	a
69	1a	Me	a
70	1a	Me	a
71	1a	Me	a
72	9b	Me	a
73	4a	Me	a
74	1a	Me	a
75	1a	Me	a
76	1a	Me	a
77	1a	Me	a
78	1a	Me	a
79	1a	Me	a
80	1a	Me	a
81	1a	Me	a
82	1a	Me	a
83	1a	Me	a
84	1a	Me	a
85	1a	Me	a
86	1a	Me	a
87	1a	Me	a
88	1a	Me	a
89	1a	Me	a
90	1a	Me	a
91	1a	Me	a
92	1a	Me	a
93	1a	Me	a
94	1a	Me	a
95	1a	Me	a
96	1a	Me	a
97	1a	Me	a
98	3a	Me	a
99	1a	Me	a
100	1a	Me	a
101	1a	Me	a
102	1a	Me	a
103	1a	Me	a
104	1a	Me	a
105	1a	Me	a
106	1a	Me	a
107	9b	Me	a
108	9b	Me	a
109	1a	Me	a
110	9b	Me	a
111	1a	Me	a
112	9b	Me	a
113	2a	Me	a
114	1a	Me	a
115	1a	Me	a
116	1a	Me	a
117	1a	Me	a
118	1a	Me	a
119	1a	Me	a
120	1a	Me	a
121	1a	Me	a
122	1a	Me	a
123	1a	Me	a
124	9b	Me	a
125	9b	Me	a
126	1a	Me	a
127	1a	Me	a
128	1a	Me	a
129	1a	Me	a
130	1a	Me	a
131	1a	Me	a
132	1a	Me	a
133	1a	Me	a
134	1a	Me	a
135	1a	Me	a
136	1a	Me	a
137	9b	Me	a
138	1a	Me	a
139	1a	Me	a
140	1a	Me	a
141	1a	Me	a
142	1a	Me	a
143	1a	Me	a
144	1a	Me	a
145	1a	Me	a
146	1a	Me	a
147	1a	Me	a
148	1a	Me	a
149	1a	Me	a
150	1a	Me	a
151	9b	Me	a
152	1a	Me	a
153	1a	Me	a
154	1a	Me	a
155	1a	Me	a
156	1a	Me	a
157	1a	Me	a
158	1a	Me	a
159	1a	Me	a
160	1a	Me	a
161	1a	Me	a
162	1a	Me	a
163	1a	Me	a
164	1a	Me	a
\.


--
-- Data for Name: mu_stud; Type: TABLE DATA; Schema: public; Owner: phimar
--

COPY public.mu_stud (studid, name, fname, klass) FROM stdin;
100	Me	\N	1a
200	You	\N	2a
101	Philippe	\N	1a
901	Tatyana	\N	9b
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: phimar
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: phimar
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: phimar
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 36, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: phimar
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: phimar
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 2, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: phimar
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: phimar
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: phimar
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 9, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: phimar
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 40, true);


--
-- Name: mu_multi_testid_seq; Type: SEQUENCE SET; Schema: public; Owner: phimar
--

SELECT pg_catalog.setval('public.mu_multi_testid_seq', 12, true);


--
-- Name: mu_results_id_seq; Type: SEQUENCE SET; Schema: public; Owner: phimar
--

SELECT pg_catalog.setval('public.mu_results_id_seq', 164, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: mu_multi mu_multi_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.mu_multi
    ADD CONSTRAINT mu_multi_pkey PRIMARY KEY (testid);


--
-- Name: mu_results mu_results_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.mu_results
    ADD CONSTRAINT mu_results_pkey PRIMARY KEY (id);


--
-- Name: mu_stud mu_stud_pkey; Type: CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.mu_stud
    ADD CONSTRAINT mu_stud_pkey PRIMARY KEY (studid);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: mu_multi_studid_id_0b2e8096; Type: INDEX; Schema: public; Owner: phimar
--

CREATE INDEX mu_multi_studid_id_0b2e8096 ON public.mu_multi USING btree (studid_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mu_multi mu_multi_studid_id_0b2e8096_fk_mu_stud_stuid; Type: FK CONSTRAINT; Schema: public; Owner: phimar
--

ALTER TABLE ONLY public.mu_multi
    ADD CONSTRAINT mu_multi_studid_id_0b2e8096_fk_mu_stud_stuid FOREIGN KEY (studid_id) REFERENCES public.mu_stud(studid) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

