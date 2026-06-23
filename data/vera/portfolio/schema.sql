PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS sources (
  source_id TEXT PRIMARY KEY,
  source_name TEXT NOT NULL,
  source_type TEXT NOT NULL,
  url TEXT,
  collected_at TEXT NOT NULL,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS products (
  sku TEXT PRIMARY KEY,
  product_name TEXT NOT NULL,
  brand TEXT NOT NULL,
  product_line TEXT,
  business_category TEXT NOT NULL,
  natura_category TEXT,
  audience TEXT,
  volume_value REAL,
  volume_unit TEXT,
  official_url TEXT NOT NULL,
  source_id TEXT NOT NULL,
  collection_date TEXT NOT NULL,
  lifecycle_status TEXT DEFAULT 'active',
  notes TEXT,
  FOREIGN KEY (source_id) REFERENCES sources(source_id)
);

CREATE TABLE IF NOT EXISTS offers (
  offer_id TEXT PRIMARY KEY,
  sku TEXT NOT NULL,
  collected_at TEXT NOT NULL,
  price_cents INTEGER,
  currency TEXT DEFAULT 'BRL',
  in_stock INTEGER,
  rating_value REAL,
  review_count INTEGER,
  offer_notes TEXT,
  FOREIGN KEY (sku) REFERENCES products(sku)
);

CREATE TABLE IF NOT EXISTS product_facts (
  fact_id TEXT PRIMARY KEY,
  sku TEXT NOT NULL,
  fact_type TEXT NOT NULL,
  fact_text TEXT NOT NULL,
  evidence_level TEXT NOT NULL,
  needs_verification INTEGER DEFAULT 0,
  publishable INTEGER DEFAULT 1,
  compliance_note TEXT,
  FOREIGN KEY (sku) REFERENCES products(sku)
);

CREATE TABLE IF NOT EXISTS sales_profiles (
  profile_id TEXT PRIMARY KEY,
  sku TEXT NOT NULL,
  client_ideal TEXT,
  positioning TEXT,
  sales_hook TEXT,
  recommended_use TEXT,
  main_objection TEXT,
  FOREIGN KEY (sku) REFERENCES products(sku)
);

CREATE TABLE IF NOT EXISTS diagnostic_questions (
  question_id TEXT PRIMARY KEY,
  sku TEXT,
  scope TEXT NOT NULL,
  question_text TEXT NOT NULL,
  stage TEXT DEFAULT 'discovery',
  FOREIGN KEY (sku) REFERENCES products(sku)
);

CREATE TABLE IF NOT EXISTS objections (
  objection_id TEXT PRIMARY KEY,
  sku TEXT NOT NULL,
  objection_text TEXT NOT NULL,
  response_text TEXT NOT NULL,
  risk_level TEXT DEFAULT 'low',
  compliance_note TEXT,
  FOREIGN KEY (sku) REFERENCES products(sku)
);

CREATE TABLE IF NOT EXISTS campaign_ideas (
  campaign_id TEXT PRIMARY KEY,
  sku TEXT,
  theme TEXT NOT NULL,
  channel TEXT NOT NULL,
  format TEXT NOT NULL,
  hook TEXT NOT NULL,
  content_angle TEXT,
  cta TEXT,
  status TEXT DEFAULT 'draft',
  compliance_status TEXT DEFAULT 'needs_review',
  FOREIGN KEY (sku) REFERENCES products(sku)
);

CREATE TABLE IF NOT EXISTS combos (
  combo_id TEXT PRIMARY KEY,
  combo_name TEXT NOT NULL,
  target_customer TEXT,
  use_case TEXT,
  commercial_note TEXT,
  compliance_note TEXT
);

CREATE TABLE IF NOT EXISTS combo_items (
  combo_id TEXT NOT NULL,
  sku TEXT NOT NULL,
  product_role TEXT,
  PRIMARY KEY (combo_id, sku),
  FOREIGN KEY (combo_id) REFERENCES combos(combo_id),
  FOREIGN KEY (sku) REFERENCES products(sku)
);

CREATE TABLE IF NOT EXISTS compliance_rules (
  rule_id TEXT PRIMARY KEY,
  sku TEXT,
  scope TEXT NOT NULL,
  severity TEXT DEFAULT 'medium',
  rule_text TEXT NOT NULL,
  required_action TEXT,
  FOREIGN KEY (sku) REFERENCES products(sku)
);

CREATE TABLE IF NOT EXISTS verification_tasks (
  task_id TEXT PRIMARY KEY,
  sku TEXT,
  owner_agent TEXT NOT NULL,
  priority TEXT DEFAULT 'medium',
  task_type TEXT NOT NULL,
  question TEXT NOT NULL,
  status TEXT DEFAULT 'open',
  due_context TEXT,
  FOREIGN KEY (sku) REFERENCES products(sku)
);

CREATE TABLE IF NOT EXISTS agent_workstreams (
  workstream_id TEXT PRIMARY KEY,
  agent_name TEXT NOT NULL,
  scope TEXT NOT NULL,
  expected_output TEXT NOT NULL,
  first_next_step TEXT,
  status TEXT DEFAULT 'active'
);
