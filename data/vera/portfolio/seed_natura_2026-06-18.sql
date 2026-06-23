PRAGMA foreign_keys = ON;

INSERT OR REPLACE INTO sources (source_id, source_name, source_type, url, collected_at, notes) VALUES
('src_natura_2026_06_18', 'Paginas oficiais Natura informadas pelo usuario', 'official_product_pages', 'https://www.natura.com.br/', '2026-06-18', 'Snapshot inicial do portfolio Vera. Precos, estoque, avaliacoes e claims devem ser verificados novamente antes de publicacao ou venda.');

INSERT OR REPLACE INTO products (
  sku, product_name, brand, product_line, business_category, natura_category,
  audience, volume_value, volume_unit, official_url, source_id, collection_date, lifecycle_status, notes
) VALUES
('NATBRA-83314', 'Desodorante Perfume Ilía Secreto Feminino 50 ml', 'Ilía', 'Ilía Secreto', 'perfumaria', 'perfumaria', 'feminino', 50, 'ml', 'https://www.natura.com.br/p/desodorante-perfume-ilia-secreto-feminino-50-ml/NATBRA-83314', 'src_natura_2026_06_18', '2026-06-18', 'active', 'Produto de perfumaria feminina com posicionamento sofisticado e marcante.'),
('NATBRA-171117', 'Desodorante Colônia Kaiak Aventura Intensa Masculino 100 ml', 'Kaiak', 'Kaiak Aventura Intensa', 'perfumaria', 'perfumaria', 'masculino', 100, 'ml', 'https://www.natura.com.br/p/desodorante-colonia-kaiak-aventura-intensa-masculino-100-ml/NATBRA-171117', 'src_natura_2026_06_18', '2026-06-18', 'active', 'Produto de perfumaria masculina com apelo de frescor, aventura e edicao limitada.'),
('NATBRA-134189', 'Multiprotetor Antissinais FPS 50 Chronos 50 ml', 'Chronos', 'Chronos', 'skincare', 'corpo e banho', 'unissex', 50, 'ml', 'https://www.natura.com.br/p/multiprotetor-antissinais-fps-50-chronos-50-ml/NATBRA-134189', 'src_natura_2026_06_18', '2026-06-18', 'active', 'Produto de protecao diaria; beneficios oficiais completos ainda precisam de verificacao.'),
('NATBRA-169233', 'Sérum Intensivo Preenchedor Hidratante Chronos Derma 30 ml', 'Chronos Derma', 'Chronos Derma', 'skincare', 'rosto', 'unissex', 30, 'ml', 'https://www.natura.com.br/p/serum-intensivo-preenchedor-hidratante-chronos-derma-30-ml/NATBRA-169233', 'src_natura_2026_06_18', '2026-06-18', 'active', 'Produto de tratamento com claims numericos que exigem preservacao de notas/rodapes oficiais.'),
('NATBRA-133503', 'Água Micelar Demaquilante Suave Chronos Derma 150 ml', 'Chronos Derma', 'Chronos Derma', 'skincare', 'maquiagem', 'unissex', 150, 'ml', 'https://www.natura.com.br/p/agua-micelar-demaquilante-suave-chronos-derma-150-ml/NATBRA-133503', 'src_natura_2026_06_18', '2026-06-18', 'active', 'Produto de limpeza/demaquilante; beneficios oficiais completos ainda precisam de verificacao.');

INSERT OR REPLACE INTO offers (
  offer_id, sku, collected_at, price_cents, currency, in_stock, rating_value, review_count, offer_notes
) VALUES
('offer_2026_06_18_83314', 'NATBRA-83314', '2026-06-18', 19990, 'BRL', 1, 4.7, 1152, 'Preco e avaliacao coletados na pagina oficial. Verificar antes de publicar.'),
('offer_2026_06_18_171117', 'NATBRA-171117', '2026-06-18', 19990, 'BRL', 1, 4.8, 96, 'Preco e avaliacao coletados na pagina oficial. Verificar antes de publicar.'),
('offer_2026_06_18_134189', 'NATBRA-134189', '2026-06-18', 11000, 'BRL', 1, 4.6, 58, 'Preco e avaliacao coletados na pagina oficial. Verificar antes de publicar.'),
('offer_2026_06_18_169233', 'NATBRA-169233', '2026-06-18', 20500, 'BRL', 1, 5.0, 12, 'Preco e avaliacao coletados na pagina oficial. Verificar antes de publicar.'),
('offer_2026_06_18_133503', 'NATBRA-133503', '2026-06-18', 8500, 'BRL', 1, 4.9, 9, 'Preco e avaliacao coletados na pagina oficial. Verificar antes de publicar.');

INSERT OR REPLACE INTO product_facts (
  fact_id, sku, fact_type, fact_text, evidence_level, needs_verification, publishable, compliance_note
) VALUES
('fact_83314_positioning', 'NATBRA-83314', 'positioning', 'Fragrancia feminina sofisticada, intensa e marcante, com contraste entre forca e delicadeza.', 'official_page_summary', 0, 1, 'Usar como linguagem consultiva, sem afirmar resultado igual para todas as pessoas.'),
('fact_83314_notes', 'NATBRA-83314', 'olfactory_notes', 'Flores brancas, fava-tonka e cafe arabica; floral adocicado intenso.', 'official_page', 0, 1, 'Confirmar piramide completa antes de detalhar notas de topo/corpo/fundo.'),
('fact_83314_fixation', 'NATBRA-83314', 'performance_claim', 'A pagina cita fixacao media de 10 horas, variavel conforme pele e ambiente.', 'official_page', 0, 1, 'Nunca prometer fixacao garantida.'),
('fact_171117_family', 'NATBRA-171117', 'olfactory_family', 'Familia olfativa aromatica; subfamilia frutal.', 'official_page', 0, 1, NULL),
('fact_171117_notes', 'NATBRA-171117', 'olfactory_notes', 'Frutas aquosas, notas aromaticas, madeiras umidas e pimentas.', 'official_page', 0, 1, NULL),
('fact_171117_limited', 'NATBRA-171117', 'commercial_flag', 'A pagina apresenta o produto como edicao limitada.', 'official_page', 1, 1, 'Verificar se a edicao limitada ainda esta vigente no dia da campanha.'),
('fact_171117_packaging', 'NATBRA-171117', 'packaging', 'A pagina cita embalagem feita com material reciclado.', 'official_page', 0, 1, 'Nao ampliar para promessas ambientais nao declaradas.'),
('fact_134189_fps', 'NATBRA-134189', 'protection_claim', 'A pagina/titulo menciona FPS 50 e FPUVA 18.', 'official_page_title', 1, 1, 'Confirmar modo de uso, reaplicacao e advertencias oficiais antes de publicar.'),
('fact_134189_reviews', 'NATBRA-134189', 'review_signal', 'Avaliacoes citam hidratacao, toque seco e conforto sob maquiagem.', 'review_excerpt', 0, 1, 'Comunicar como relato de clientes, nao promessa oficial da marca.'),
('fact_169233_ha', 'NATBRA-169233', 'ingredient_claim', 'A pagina cita +75% acido hialuronico para a pele.', 'official_page', 0, 1, 'Preservar notas/rodapes oficiais.'),
('fact_169233_hydration', 'NATBRA-169233', 'result_claim', 'A pagina cita 100% pele mais hidratada e fortalecida em ate 14 dias.', 'official_page', 0, 1, 'Preservar notas/rodapes oficiais.'),
('fact_169233_fill', 'NATBRA-169233', 'result_claim', 'A pagina cita +92% preenchimento imediato.', 'official_page', 0, 1, 'Preservar notas/rodapes oficiais; nao prometer eliminacao definitiva de rugas.'),
('fact_169233_derm', 'NATBRA-169233', 'proof_claim', 'A pagina cita resultados comprovados por dermatologistas.', 'official_page', 0, 1, 'Nao transformar em promessa medica.'),
('fact_133503_category', 'NATBRA-133503', 'category_signal', 'O schema da pagina classifica o produto em maquiagem.', 'official_schema', 0, 1, NULL),
('fact_133503_gap', 'NATBRA-133503', 'verification_gap', 'Beneficios oficiais completos, modo de uso, tipo de pele, remocao de maquiagem a prova d''agua e enxague precisam ser verificados.', 'agent_analysis', 1, 0, 'Nao publicar beneficios ainda.');

INSERT OR REPLACE INTO sales_profiles (
  profile_id, sku, client_ideal, positioning, sales_hook, recommended_use, main_objection
) VALUES
('profile_83314', 'NATBRA-83314', 'Cliente que busca perfumaria intensa, floral adocicada e imagem de sofisticacao/confiança.', 'Perfume feminino sofisticado, marcante e enigmatico.', 'Flores brancas, fava-tonka e cafe arabica para uma presenca elegante.', 'Noite, ocasioes especiais, outono/inverno ou uso diario para quem gosta de fragrancia presente.', 'Medo de ser forte ou doce demais.'),
('profile_171117', 'NATBRA-171117', 'Cliente que gosta de fragrancia fresca, aromatica e frutal para dia a dia ou para sair.', 'Deo colonia masculina fresca com energia de aventura.', 'Frutas aquosas, madeiras umidas e pimentas em edicao limitada.', 'Dia a dia, trabalho, saida casual e presente masculino.', 'Receio de Kaiak parecer comum ou durar pouco.'),
('profile_134189', 'NATBRA-134189', 'Cliente que procura protecao facial FPS 50 com acabamento confortavel.', 'Protetor diario com proposta antissinais.', 'FPS 50/FPUVA 18 e reviews citando toque seco sob maquiagem.', 'Ultimo passo da rotina da manha.', 'Medo de oleosidade ou textura pesada.'),
('profile_169233', 'NATBRA-169233', 'Cliente focado em hidratacao, preenchimento imediato e sinais como rugas/linhas finas.', 'Tratamento com acido hialuronico e claims de hidratacao/preenchimento.', '+75% acido hialuronico, hidratacao em ate 14 dias e +92% preenchimento imediato.', 'Depois da limpeza e antes do protetor pela manha; depois da limpeza a noite.', 'Preco alto ou expectativa de tirar rugas.'),
('profile_133503', 'NATBRA-133503', 'Cliente que usa maquiagem ou busca etapa de limpeza/demaquilante suave.', 'Limpeza inicial e remocao de maquiagem na rotina facial.', 'Agua micelar suave Chronos Derma com avaliacao alta no snapshot.', 'Primeiro passo da rotina, especialmente a noite.', 'Falta de clareza sobre beneficios oficiais, tipo de pele e necessidade de enxague.');

INSERT OR REPLACE INTO diagnostic_questions (
  question_id, sku, scope, question_text, stage
) VALUES
('q_global_01', NULL, 'portfolio', 'Voce esta procurando perfume, skincare ou um combo?', 'discovery'),
('q_global_02', NULL, 'perfumaria', 'Para perfume, prefere algo mais intenso ou mais leve?', 'discovery'),
('q_global_03', NULL, 'perfumaria', 'Voce gosta de fragrancias florais adocicadas?', 'discovery'),
('q_global_04', NULL, 'perfumaria', 'O perfume seria para uso diario, para sair ou para presentear?', 'discovery'),
('q_global_05', NULL, 'perfumaria', 'Voce prefere uma fragrancia sofisticada/enigmatica ou fresca/aromatica?', 'discovery'),
('q_global_06', NULL, 'skincare', 'Na rotina facial, voce ja usa protetor todos os dias?', 'discovery'),
('q_global_07', NULL, 'skincare', 'Voce usa maquiagem por cima do protetor?', 'discovery'),
('q_global_08', NULL, 'skincare', 'Sua prioridade hoje e hidratacao, preenchimento, sinais, linhas finas, limpeza ou demaquilante?', 'discovery'),
('q_global_09', NULL, 'portfolio', 'Voce prefere produto com muitas avaliacoes ou aceita testar novidades?', 'qualification'),
('q_global_10', NULL, 'skincare', 'Quer montar uma rotina simples com limpeza, tratamento e protecao?', 'qualification');

INSERT OR REPLACE INTO objections (
  objection_id, sku, objection_text, response_text, risk_level, compliance_note
) VALUES
('obj_83314_strong', 'NATBRA-83314', 'Tenho medo de ser forte demais.', 'Ele e intenso e marcante; vale comecar com poucas borrifadas e testar na pele.', 'low', 'Nao prometer que ficara suave em todas as peles.'),
('obj_83314_sweet', 'NATBRA-83314', 'Perfume doce me enjoa.', 'Ele tem lado floral adocicado, entao e melhor provar antes. A fava-tonka e o cafe arabica dao personalidade.', 'low', 'Evitar afirmar que nao enjoa.'),
('obj_83314_fixation', 'NATBRA-83314', 'Fixa mesmo 10 horas?', 'A pagina cita fixacao media de 10 horas, mas isso varia por pele, clima e quantidade aplicada.', 'medium', 'Nao prometer fixacao garantida.'),
('obj_171117_common', 'NATBRA-171117', 'Kaiak e muito comum.', 'Esse e o Aventura Intensa, edicao limitada com frutas aquosas, madeiras umidas e pimentas.', 'low', 'Verificar status da edicao limitada.'),
('obj_171117_duration', 'NATBRA-171117', 'Sera que dura?', 'Ele e deo colonia; desempenho varia por pele e ambiente. A aplicacao nos pontos indicados ajuda na perfumacao.', 'medium', 'Nao prometer duracao.'),
('obj_134189_oily', 'NATBRA-134189', 'Tenho medo de ficar oleoso.', 'Algumas avaliacoes da pagina citam toque seco e que nao fica pesado sob maquiagem, mas vale testar na sua pele.', 'medium', 'Tratar como review, nao promessa oficial.'),
('obj_169233_price', 'NATBRA-169233', 'R$205 e caro.', 'Ele e o produto de tratamento da rotina. Se a prioridade for hidratacao, linhas finas e pele mais fortalecida, ele vira o investimento central.', 'low', 'Evitar promessa de resultado garantido.'),
('obj_169233_wrinkles', 'NATBRA-169233', 'Esse serum tira rugas?', 'A linguagem correta e que ajuda a preencher, hidratar e reduzir a aparencia de rugas e linhas finas, conforme a descricao oficial. Nao e tratamento medico.', 'high', 'Nao usar linguagem medica ou definitiva.'),
('obj_133503_need', 'NATBRA-133503', 'Nao sei se preciso de agua micelar.', 'Ela pode fazer sentido se voce usa maquiagem ou quer uma etapa simples de limpeza; beneficios oficiais ainda precisam ser confirmados antes de uma recomendacao completa.', 'medium', 'Nao afirmar beneficios nao verificados.');

INSERT OR REPLACE INTO campaign_ideas (
  campaign_id, sku, theme, channel, format, hook, content_angle, cta, status, compliance_status
) VALUES
('camp_83314_presence', 'NATBRA-83314', 'Sofisticacao e presenca', 'Instagram', 'reel', 'Perfume para quem quer sofisticacao e presenca.', 'Mostrar Ilia como floral adocicado intenso para noites e ocasioes especiais.', 'Me chama para ver se combina com voce.', 'draft', 'needs_review'),
('camp_171117_fresh', 'NATBRA-171117', 'Frescor com intensidade', 'Instagram', 'reel', 'Kaiak Aventura Intensa: aromatico frutal para dia a dia e para sair.', 'Comparar frescor, frutas aquosas e madeiras umidas.', 'Quer uma opcao masculina versatil? Me chama.', 'draft', 'needs_review'),
('camp_perfume_compare', NULL, 'Comparativo de fragrancias', 'Instagram', 'carousel', 'Floral adocicado intenso x aromatico frutal.', 'Ajudar o cliente a escolher entre Ilia e Kaiak por gosto e ocasiao.', 'Responda qual estilo voce prefere.', 'draft', 'needs_review'),
('camp_chronos_3steps', NULL, 'Rotina Chronos em 3 passos', 'Instagram', 'carousel', 'Limpar, tratar e proteger.', 'Organizar Agua Micelar, Serum e Multiprotetor em rotina simples.', 'Me chama para montar sua rotina.', 'draft', 'blocked_until_verified'),
('camp_134189_reviews', 'NATBRA-134189', 'Reviews sobre acabamento', 'Stories', 'sequencia', 'O que clientes citam sobre o Multiprotetor Chronos FPS 50.', 'Usar relatos de hidratacao, toque seco e maquiagem como sinal de review.', 'Quer que eu confirme preco e estoque de hoje?', 'draft', 'needs_review'),
('camp_169233_ha', 'NATBRA-169233', 'Acido hialuronico', 'Instagram', 'reel', 'Serum Chronos Derma: hidratacao e preenchimento imediato.', 'Explicar claims oficiais com notas ¹²³ preservadas.', 'Me chama para entender se ele combina com sua rotina.', 'draft', 'needs_review'),
('camp_gift_style', NULL, 'Presente por estilo', 'WhatsApp', 'lista', 'Como escolher presente Natura pelo estilo da pessoa.', 'Separar presente sofisticado, fresco, rotina facial e combo casal.', 'Me diga o perfil da pessoa que eu sugiro um combo.', 'draft', 'needs_review'),
('camp_ratings', NULL, 'Produtos com boas avaliacoes', 'Instagram', 'carousel', 'Notas, precos e para quem indicar.', 'Mostrar rating/review count como snapshot de 2026-06-18.', 'Consulte preco atualizado antes de comprar.', 'draft', 'needs_review');

INSERT OR REPLACE INTO combos (
  combo_id, combo_name, target_customer, use_case, commercial_note, compliance_note
) VALUES
('combo_perfume_feminino_skincare', 'Perfume feminino + skincare', 'Cliente que quer cuidado e presenca para ocasioes especiais.', 'Presente ou autocuidado', 'Ilia Secreto + Serum Chronos Derma.', 'Preservar claims do serum.'),
('combo_masculino_presenteavel', 'Masculino presenteavel', 'Cliente buscando presente masculino versatil.', 'Presente masculino', 'Kaiak Aventura Intensa + Multiprotetor Chronos FPS 50.', 'Confirmar beneficios oficiais do Multiprotetor antes de publicar.'),
('combo_rotina_facial_chronos', 'Rotina facial Chronos', 'Cliente que quer rotina simples de limpar, tratar e proteger.', 'Rotina skincare', 'Agua Micelar + Serum + Multiprotetor.', 'Bloquear campanha ate verificar beneficios da Agua Micelar e Multiprotetor.'),
('combo_maquiagem_pele', 'Maquiagem e pele', 'Cliente que usa maquiagem e quer limpeza + protecao.', 'Rotina com maquiagem', 'Agua Micelar + Multiprotetor FPS 50.', 'Uso sob maquiagem vem de reviews, nao de promessa oficial.'),
('combo_casal_presente_duplo', 'Casal / presente duplo', 'Cliente comprando dois presentes ou combo casal.', 'Presente duplo', 'Ilia Secreto + Kaiak Aventura Intensa.', 'Evitar linguagem estereotipada; vender por gosto/ocasiao.');

INSERT OR REPLACE INTO combo_items (combo_id, sku, product_role) VALUES
('combo_perfume_feminino_skincare', 'NATBRA-83314', 'fragrancia'),
('combo_perfume_feminino_skincare', 'NATBRA-169233', 'tratamento'),
('combo_masculino_presenteavel', 'NATBRA-171117', 'fragrancia'),
('combo_masculino_presenteavel', 'NATBRA-134189', 'cuidado_diario'),
('combo_rotina_facial_chronos', 'NATBRA-133503', 'limpeza'),
('combo_rotina_facial_chronos', 'NATBRA-169233', 'tratamento'),
('combo_rotina_facial_chronos', 'NATBRA-134189', 'protecao'),
('combo_maquiagem_pele', 'NATBRA-133503', 'limpeza'),
('combo_maquiagem_pele', 'NATBRA-134189', 'protecao'),
('combo_casal_presente_duplo', 'NATBRA-83314', 'fragrancia_floral_adocicada'),
('combo_casal_presente_duplo', 'NATBRA-171117', 'fragrancia_fresca_aromatica');

INSERT OR REPLACE INTO compliance_rules (
  rule_id, sku, scope, severity, rule_text, required_action
) VALUES
('rule_global_refresh', NULL, 'portfolio', 'high', 'Precos, estoque, avaliacoes, selos e edicao limitada podem mudar.', 'Verificar pagina oficial no dia de publicacao ou venda.'),
('rule_perfume_fixation', NULL, 'perfumaria', 'high', 'Nao prometer fixacao, projecao ou duracao garantida.', 'Usar linguagem: varia por pele, clima e quantidade aplicada.'),
('rule_kaiak_sustainability', 'NATBRA-171117', 'sustentabilidade', 'medium', 'Nao ampliar a informacao de embalagem com material reciclado para promessas ambientais maiores.', 'Repetir apenas o claim oficial confirmado.'),
('rule_chronos_fps', 'NATBRA-134189', 'protecao_solar', 'high', 'Modo de uso, reaplicacao, FPUVA/FPS e advertencias oficiais precisam ser confirmados antes de campanha.', 'Bloquear conteudo ate verificacao oficial.'),
('rule_serum_claims', 'NATBRA-169233', 'skincare_claims', 'high', 'Claims numericos do serum exigem notas/rodapes ¹²³ e nao podem virar promessa medica.', 'Preservar rodapes e usar termos como ajuda, aparencia e rotina de cuidado.'),
('rule_reviews', NULL, 'reviews', 'medium', 'Reviews devem ser comunicados como relatos de clientes, nao como promessa oficial da marca.', 'Usar clientes citam ou avaliacoes mencionam.'),
('rule_micellar_gap', 'NATBRA-133503', 'skincare_claims', 'high', 'Beneficios oficiais da agua micelar nao estao completos neste snapshot.', 'Verificar antes de publicar beneficios.');

INSERT OR REPLACE INTO verification_tasks (
  task_id, sku, owner_agent, priority, task_type, question, status, due_context
) VALUES
('task_134189_benefits', 'NATBRA-134189', 'agente_skincare', 'high', 'official_claim_check', 'Quais sao os beneficios oficiais completos do Multiprotetor Antissinais FPS 50 Chronos?', 'open', 'Antes de qualquer post ou script de venda.'),
('task_134189_usage', 'NATBRA-134189', 'agente_skincare', 'high', 'usage_check', 'Qual e o modo de uso, reaplicacao e advertencias oficiais do protetor?', 'open', 'Antes de campanha de protecao solar.'),
('task_133503_benefits', 'NATBRA-133503', 'agente_skincare', 'high', 'official_claim_check', 'Quais sao os beneficios oficiais completos da Agua Micelar Demaquilante Suave Chronos Derma?', 'open', 'Antes de publicar rotina Chronos.'),
('task_133503_usage', 'NATBRA-133503', 'agente_skincare', 'medium', 'usage_check', 'A agua micelar exige enxague? Remove maquiagem a prova d''agua? Qual tipo de pele indicado?', 'open', 'Antes de atendimento consultivo detalhado.'),
('task_171117_limited', 'NATBRA-171117', 'agente_perfumaria', 'medium', 'availability_check', 'A edicao limitada do Kaiak Aventura Intensa ainda esta vigente?', 'open', 'Antes de campanha com urgencia.'),
('task_prices_refresh', NULL, 'agente_conteudo_vendas', 'high', 'offer_refresh', 'Atualizar preco, estoque, rating e review count dos cinco produtos.', 'open', 'No dia de publicacao ou envio de oferta.');

INSERT OR REPLACE INTO agent_workstreams (
  workstream_id, agent_name, scope, expected_output, first_next_step, status
) VALUES
('ws_perfumaria', 'agente_perfumaria', 'Ilia Secreto e Kaiak Aventura Intensa', '3 scripts de WhatsApp, 3 stories e 2 reels para perfumaria.', 'Transformar sales_profiles, objections e product_facts de perfumaria em copys curtas.', 'active'),
('ws_skincare', 'agente_skincare', 'Chronos e Chronos Derma', 'Rotina consultiva, verificacao de lacunas e revisao de claims.', 'Resolver verification_tasks de Multiprotetor e Agua Micelar.', 'active'),
('ws_conteudo_vendas', 'agente_conteudo_vendas', 'Portfolio completo', 'Calendario de 7 dias com CTA de atendimento.', 'Usar campaign_ideas e combos para criar sequencia semanal.', 'active'),
('ws_atendimento', 'agente_atendimento', 'Perguntas, objecoes e respostas', 'Respostas curtas para atendimento consultivo por WhatsApp.', 'Converter diagnostic_questions e objections em blocos reutilizaveis.', 'active'),
('ws_compliance', 'agente_compliance', 'Claims, reviews, preco e protecao solar', 'Aprovacao ou bloqueio de copys antes de publicacao.', 'Aplicar compliance_rules em toda campanha marcada needs_review.', 'active');
