#!/usr/bin/env python3
"""Generate 17 distinct, visually diverse diagram topologies for AWS Cognito course."""

DIAGRAMS = {
    # 1. Two-Plane Architecture Map: CIAM Plane vs AWS Cloud Plane
    "ru/index.html": {
        "num": 1,
        "title": "Архитектурная модель сервиса: User Pools (каталог и токены) против Identity Pools (роли STS).",
        "aria": "Схема двух плоскостей архитектуры Cognito: User Pools и Identity Pools",
        "h": 230,
        "content": """  <!-- Top Client Banner -->
  <rect x="30" y="8" width="260" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Клиент (Web / Mobile App)</text>

  <!-- Down to User Pool -->
  <line x1="80" y1="34" x2="80" y2="46" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="80,52 76,44 84,44" fill="currentColor"/>

  <!-- Left Plane: User Pools CIAM -->
  <rect x="15" y="52" width="130" height="110" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="80" y="72" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">User Pool (CIAM)</text>
  <text x="80" y="90" text-anchor="middle" font-size="12" fill="currentColor">Аутентификация</text>
  <text x="80" y="106" text-anchor="middle" font-size="12" fill="currentColor">База профилей</text>
  <text x="80" y="124" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Выпуск токенов</text>
  <text x="80" y="146" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">ID • Access</text>

  <!-- Cross-Plane Exchange: User Pool to Identity Pool -->
  <line x1="145" y1="107" x2="167" y2="107" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="175,107 167,103 167,111" fill="currentColor"/>

  <!-- Right Plane: Identity Pools & STS -->
  <rect x="175" y="52" width="130" height="110" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="240" y="72" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Identity Pool</text>
  <text x="240" y="90" text-anchor="middle" font-size="12" fill="currentColor">Федерация с IdP</text>
  <text x="240" y="106" text-anchor="middle" font-size="12" fill="currentColor">STS ключи</text>
  <text x="240" y="124" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">IAM роли</text>
  <text x="240" y="146" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">SigV4 сессии</text>

  <!-- Down to AWS Cloud Services -->
  <line x1="240" y1="162" x2="240" y2="178" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="240,184 236,176 244,176" fill="currentColor"/>

  <!-- Bottom Banner: AWS Services -->
  <rect x="175" y="184" width="130" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="240" y="199" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Ресурсы AWS</text>
  <text x="240" y="211" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">S3 • DynamoDB</text>"""
    },

    # 2. 3-Pillar Component Directory Breakdown
    "ru/01.html": {
        "num": 2,
        "title": "Анатомия каталога User Pool: структура атрибутов, политики паролей и верификация.",
        "aria": "Схема трех столпов каталога User Pool: атрибуты, политики и доставка",
        "h": 230,
        "content": """  <!-- Top Directory Core -->
  <rect x="30" y="8" width="260" height="28" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Каталог Amazon Cognito User Pool</text>

  <!-- 3 Pillar Arrows Down -->
  <line x1="59" y1="36" x2="59" y2="54" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="59,60 55,52 63,52" fill="currentColor"/>

  <line x1="160" y1="36" x2="160" y2="54" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,60 156,52 164,52" fill="currentColor"/>

  <line x1="261" y1="36" x2="261" y2="54" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="261,60 257,52 265,52" fill="currentColor"/>

  <!-- 3 Pillars -->
  <rect x="12" y="60" width="94" height="95" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="59" y="78" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Атрибуты</text>
  <text x="59" y="98" text-anchor="middle" font-size="12" fill="currentColor">Схема полей</text>
  <text x="59" y="116" text-anchor="middle" font-size="12" fill="currentColor">Claims</text>
  <text x="59" y="136" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Неизменяемость</text>

  <rect x="113" y="60" width="94" height="95" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="78" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Политики</text>
  <text x="160" y="98" text-anchor="middle" font-size="12" fill="currentColor">Сложность</text>
  <text x="160" y="116" text-anchor="middle" font-size="12" fill="currentColor">MFA защита</text>
  <text x="160" y="136" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">SRP-вход</text>

  <rect x="214" y="60" width="94" height="95" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="261" y="78" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Доставка</text>
  <text x="261" y="98" text-anchor="middle" font-size="12" fill="currentColor">Email OTP</text>
  <text x="261" y="116" text-anchor="middle" font-size="12" fill="currentColor">SMS OTP</text>
  <text x="261" y="136" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">SES / SNS</text>

  <!-- Down to Bottom Outcome -->
  <line x1="160" y1="155" x2="160" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,180 156,172 164,172" fill="currentColor"/>

  <!-- Bottom Banner: Confirmed State -->
  <rect x="30" y="180" width="260" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="196" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Статус CONFIRMED</text>
  <text x="160" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Готовый к авторизации профиль</text>"""
    },

    # 3. Circular Token Renewal Loop
    "ru/02.html": {
        "num": 3,
        "title": "Триада токенов OIDC и OAuth 2.0: ID, Access, Refresh и проверка JWKS.",
        "aria": "Схема замкнутого контура ротации токенов Refresh Token Flow",
        "h": 230,
        "content": """  <!-- Top: Client App -->
  <rect x="40" y="10" width="240" height="32" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Клиентское приложение (SPA / App)</text>
  <text x="160" y="37" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Хранение ID Token и Access Token</text>

  <!-- Top down to Right (API Gateway) -->
  <line x1="245" y1="42" x2="245" y2="70" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="245,76 241,68 249,68" fill="currentColor"/>

  <!-- Right: API Gateway 401 -->
  <rect x="175" y="76" width="130" height="42" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="240" y="93" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">API Gateway</text>
  <text x="240" y="108" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">401 Token Expired</text>

  <!-- Right down to Bottom (Cognito /oauth2/token) -->
  <line x1="245" y1="118" x2="245" y2="148" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="245,154 241,146 249,146" fill="currentColor"/>

  <!-- Bottom: Cognito Refresh Endpoint -->
  <rect x="40" y="154" width="240" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="169" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Cognito /oauth2/token</text>
  <text x="160" y="181" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Обмен Refresh Token на Access</text>

  <!-- Left: Secure Storage (RT) -->
  <rect x="15" y="76" width="130" height="42" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="80" y="93" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Secure Store</text>
  <text x="80" y="108" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Refresh Token</text>

  <!-- Bottom up to Left -->
  <line x1="80" y1="154" x2="80" y2="126" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="80,118 76,126 84,126" fill="currentColor"/>

  <!-- Left up to Top -->
  <line x1="80" y1="76" x2="80" y2="50" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="80,42 76,50 84,50" fill="currentColor"/>"""
    },

    # 4. Protocol Sequence Ladder: PKCE Authorization Code Flow
    "ru/03.html": {
        "num": 4,
        "title": "Поток Authorization Code с криптографическим протоколом PKCE.",
        "aria": "Схема протокола OAuth 2.0 PKCE в виде пошаговой диаграммы обмена",
        "h": 220,
        "content": """  <!-- Left Column: Public Client -->
  <rect x="10" y="15" width="80" height="190" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="50" y="34" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Клиент</text>
  <text x="50" y="48" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">SPA App</text>

  <!-- Right Column: Cognito Server -->
  <rect x="230" y="15" width="80" height="190" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="270" y="34" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Cognito</text>
  <text x="270" y="48" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">IdP Core</text>

  <!-- Step 1: Client -> Cognito -->
  <line x1="90" y1="75" x2="222" y2="75" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="230,75 222,71 222,79" fill="currentColor"/>
  <text x="160" y="68" text-anchor="middle" font-size="12" fill="currentColor">1. /authorize</text>

  <!-- Step 2: Cognito -> Client -->
  <line x1="230" y1="110" x2="98" y2="110" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="90,110 98,106 98,114" fill="currentColor"/>
  <text x="160" y="103" text-anchor="middle" font-size="12" fill="currentColor">2. Редирект (Code)</text>

  <!-- Step 3: Client -> Cognito -->
  <line x1="90" y1="145" x2="222" y2="145" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="230,145 222,141 222,149" fill="currentColor"/>
  <text x="160" y="138" text-anchor="middle" font-size="12" fill="currentColor">3. /token + Verifier</text>

  <!-- Step 4: Cognito -> Client -->
  <line x1="230" y1="180" x2="98" y2="180" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="90,180 98,176 98,184" fill="currentColor"/>
  <text x="160" y="173" text-anchor="middle" font-size="12" fill="currentColor">4. Токены JWT</text>"""
    },

    # 5. 4-Tier Infrastructure Stack: Hosted UI
    "ru/04.html": {
        "num": 5,
        "title": "Топология Hosted UI: CloudFront, ACM в us-east-1 и кастомный домен.",
        "aria": "Схема 4-уровневой инфраструктуры Hosted UI и кастомных доменов",
        "h": 230,
        "content": """  <!-- Layer 1: DNS -->
  <rect x="30" y="10" width="260" height="30" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="28" text-anchor="middle" font-size="12" fill="currentColor">1. Route 53 (auth.example.com)</text>

  <!-- 1 -> 2 -->
  <line x1="160" y1="40" x2="160" y2="58" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,66 156,58 164,58" fill="currentColor"/>

  <!-- Layer 2: CloudFront Edge -->
  <rect x="30" y="66" width="260" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="82" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">2. Amazon CloudFront Edge</text>
  <text x="160" y="94" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">ACM Сертификат (us-east-1)</text>

  <!-- 2 -> 3 -->
  <line x1="160" y1="100" x2="160" y2="116" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,124 156,116 164,116" fill="currentColor"/>

  <!-- Layer 3: Cognito UI Core -->
  <rect x="30" y="124" width="260" height="34" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="140" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">3. Cognito Hosted UI Engine</text>
  <text x="160" y="152" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Брендинг CSS • Вход и сессии</text>

  <!-- 3 -> 4 -->
  <line x1="160" y1="158" x2="160" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,182 156,176 164,176" fill="currentColor"/>

  <!-- Layer 4: Redirect Callback -->
  <rect x="30" y="182" width="260" height="30" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="200" text-anchor="middle" font-size="12" fill="currentColor">4. Редирект в SPA с кодом</text>"""
    },

    # 6. Fork-Join Federation Bridge
    "ru/05.html": {
        "num": 6,
        "title": "Корпоративная и социальная федерация: интеграция SAML 2.0 и OIDC с JIT.",
        "aria": "Схема моста федерации: конвергенция внешних IdP в локальный каталог",
        "h": 220,
        "content": """  <!-- Top Two IdP Sources -->
  <rect x="15" y="10" width="135" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="82" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">SAML 2.0 IdP</text>
  <text x="82" y="39" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Okta / Entra ID</text>

  <rect x="170" y="10" width="135" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="237" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">OIDC Social</text>
  <text x="237" y="39" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Google / Apple</text>

  <!-- Convergence Lines Down to Broker -->
  <line x1="82" y1="46" x2="82" y2="66" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="82,74 78,66 86,66" fill="currentColor"/>

  <line x1="237" y1="46" x2="237" y2="66" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="237,74 233,66 241,66" fill="currentColor"/>

  <!-- Middle Broker -->
  <rect x="30" y="74" width="260" height="42" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="93" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Cognito Federation Broker</text>
  <text x="160" y="107" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Маппинг claims • JIT-провижининг</text>

  <!-- Down to Unified Catalog -->
  <line x1="160" y1="116" x2="160" y2="138" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,146 156,138 164,138" fill="currentColor"/>

  <!-- Bottom Catalog -->
  <rect x="20" y="146" width="280" height="46" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="165" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Единый User Pool Каталог</text>
  <text x="160" y="181" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Связывание аккаунтов (AdminLink)</text>"""
    },

    # 7. Hub-and-Spoke Event Bus
    "ru/06.html": {
        "num": 7,
        "title": "Жизненный цикл бессерверных триггеров AWS Lambda в User Pool.",
        "aria": "Схема топологии звезда: ядро User Pool и радиальные триггеры Lambda",
        "h": 230,
        "content": """  <!-- Top Spoke: Pre Sign-up -->
  <rect x="85" y="10" width="150" height="32" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="29" text-anchor="middle" font-size="12" fill="currentColor">Pre Sign-up (Валидация)</text>

  <!-- Arrow Top to Center -->
  <line x1="160" y1="42" x2="160" y2="70" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,78 156,70 164,70" fill="currentColor"/>

  <!-- Left Spoke: Pre Token Gen -->
  <rect x="8" y="78" width="82" height="46" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="49" y="97" text-anchor="middle" font-size="12" fill="currentColor">Pre-Token</text>
  <text x="49" y="111" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Claims</text>

  <!-- Arrow Left to Center -->
  <line x1="90" y1="101" x2="98" y2="101" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="106,101 98,97 98,105" fill="currentColor"/>

  <!-- Center Hub: User Pool Core -->
  <rect x="106" y="78" width="108" height="46" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="97" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Cognito Hub</text>
  <text x="160" y="111" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Шина событий</text>

  <!-- Arrow Center to Right -->
  <line x1="214" y1="101" x2="222" y2="101" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="230,101 222,97 222,105" fill="currentColor"/>

  <!-- Right Spoke: Custom Message -->
  <rect x="230" y="78" width="82" height="46" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="271" y="97" text-anchor="middle" font-size="12" fill="currentColor">Custom</text>
  <text x="271" y="111" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Шаблоны</text>

  <!-- Arrow Center to Bottom -->
  <line x1="160" y1="124" x2="160" y2="152" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,160 156,152 164,152" fill="currentColor"/>

  <!-- Bottom Spoke: Post Confirmation -->
  <rect x="85" y="160" width="150" height="34" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="177" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Post Confirmation</text>
  <text x="160" y="188" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Запись в БД</text>"""
    },

    # 8. Stepwise Delegation Chain (Identity Pools & STS)
    "ru/07.html": {
        "num": 8,
        "title": "Обмен токенов на временные учетные данные AWS STS через Identity Pool.",
        "aria": "Схема 4-ступенчатой цепочки делегирования прав STS через Identity Pool",
        "h": 230,
        "content": """  <!-- Step 1: User Pool Token -->
  <rect x="20" y="10" width="280" height="30" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="28" text-anchor="middle" font-size="12" fill="currentColor">1. User Pool ID Token (OpenID)</text>

  <line x1="160" y1="40" x2="160" y2="58" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,66 156,58 164,58" fill="currentColor"/>

  <!-- Step 2: Identity Pool GetId -->
  <rect x="20" y="66" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="82" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">2. Identity Pool (GetId)</text>
  <text x="160" y="94" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Роли Authenticated / Unauth</text>

  <line x1="160" y1="100" x2="160" y2="116" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,124 156,116 164,116" fill="currentColor"/>

  <!-- Step 3: AWS STS -->
  <rect x="20" y="124" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="140" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">3. AWS STS (AssumeRoleWithWebIdentity)</text>
  <text x="160" y="152" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Временные ключи SessionToken</text>

  <line x1="160" y1="158" x2="160" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,182 156,176 164,176" fill="currentColor"/>

  <!-- Step 4: Direct SigV4 Call -->
  <rect x="20" y="182" width="280" height="30" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="200" text-anchor="middle" font-size="12" fill="currentColor">4. Прямой доступ к AWS (S3 / DynamoDB)</text>"""
    },

    # 9. Multi-Stage Security Funnel (WAFv2 + ASF)
    "ru/08.html": {
        "num": 9,
        "title": "Эшелонированная защита каталога: интеграция AWS WAFv2 и Cognito ASF.",
        "aria": "Схема воронки эшелонированной безопасности WAF и Cognito ASF",
        "h": 230,
        "content": """  <!-- Top: Raw Web Traffic -->
  <rect x="30" y="8" width="260" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Входящий интернет-трафик</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <!-- Level 1 Filter: AWS WAFv2 -->
  <rect x="30" y="54" width="260" height="32" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="70" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Уровень L7: AWS WAFv2 Web ACL</text>
  <text x="160" y="81" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Bot Control • Rate Limiting</text>

  <line x1="160" y1="86" x2="160" y2="100" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,106 156,98 164,98" fill="currentColor"/>

  <!-- Level 2 Filter: Cognito ASF -->
  <rect x="30" y="106" width="260" height="32" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="122" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Уровень CIAM: Cognito ASF</text>
  <text x="160" y="133" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Адаптивный риск • Утечки паролей</text>

  <!-- Fork to Actions -->
  <path d="M 160 138 L 160 152 L 85 152 L 85 164" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,170 81,162 89,162" fill="currentColor"/>

  <path d="M 160 138 L 160 152 L 235 152 L 235 164" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,170 231,162 239,162" fill="currentColor"/>

  <!-- Action Left: Step-Up MFA -->
  <rect x="15" y="170" width="140" height="38" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="85" y="187" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Низкий / Средний</text>
  <text x="85" y="200" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Allow / Вызов MFA</text>

  <!-- Action Right: Block -->
  <rect x="165" y="170" width="140" height="38" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="187" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Высокий риск</text>
  <text x="235" y="200" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Блокировка / Отказ</text>"""
    },

    # 10. Economics Pyramid: MAU & Quotas
    "ru/09.html": {
        "num": 10,
        "title": "Модель тарификации MAU, защита от SMS Toll Fraud и квоты API.",
        "aria": "Схема пирамиды расходов: MAU база, API квоты и экономия на MFA",
        "h": 230,
        "content": """  <!-- Top Wide Tier: 50K Free MAU -->
  <rect x="20" y="8" width="280" height="30" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="27" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">База MAU: 50 000 Free Tier</text>

  <line x1="160" y1="38" x2="160" y2="56" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,62 156,54 164,54" fill="currentColor"/>

  <!-- Middle Tier: API Limits & Quotas -->
  <rect x="40" y="62" width="240" height="34" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="79" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Квоты API Identity Provider</text>
  <text x="160" y="90" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Лимиты TPS • Burst емкость</text>

  <!-- Fork to Bottom Pillars -->
  <path d="M 160 96 L 160 110 L 85 110 L 85 120" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,126 81,118 89,118" fill="currentColor"/>

  <path d="M 160 96 L 160 110 L 235 110 L 235 120" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,126 231,118 239,118" fill="currentColor"/>

  <!-- Left: SMS Fraud Guard -->
  <rect x="15" y="126" width="140" height="42" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="145" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">SMS Toll Fraud</text>
  <text x="85" y="159" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Лимиты расходов SNS</text>

  <!-- Right: TOTP MFA -->
  <rect x="165" y="126" width="140" height="42" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="145" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">TOTP Аутентификатор</text>
  <text x="235" y="159" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">$0 за SMS рассылку</text>

  <!-- Dual Connectors Down to Final TCO Banner -->
  <line x1="85" y1="168" x2="85" y2="182" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,188 81,180 89,180" fill="currentColor"/>

  <line x1="235" y1="168" x2="235" y2="182" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,188 231,180 239,180" fill="currentColor"/>

  <rect x="30" y="188" width="260" height="28" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="206" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Итог: Предсказуемый TCO</text>"""
    },

    # 11. Protocol Sequence Ladder: SRP-6a Handshake
    "ru/10.html": {
        "num": 11,
        "title": "Базовая инфраструктура User Pool в Terraform и SRP-аутентификация.",
        "aria": "Схема протокола SRP-6a в виде пошаговой диаграммы без передачи пароля",
        "h": 220,
        "content": """  <!-- Left Column: Client -->
  <rect x="10" y="15" width="80" height="190" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="50" y="34" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Клиент</text>
  <text x="50" y="48" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">SRP Client</text>

  <!-- Right Column: Cognito -->
  <rect x="230" y="15" width="80" height="190" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="270" y="34" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Cognito</text>
  <text x="270" y="48" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Verifier</text>

  <!-- Step 1: Client -> Server -->
  <line x1="90" y1="75" x2="222" y2="75" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="230,75 222,71 222,79" fill="currentColor"/>
  <text x="160" y="68" text-anchor="middle" font-size="12" fill="currentColor">1. SRP_A ключ</text>

  <!-- Step 2: Server -> Client -->
  <line x1="230" y1="110" x2="98" y2="110" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="90,110 98,106 98,114" fill="currentColor"/>
  <text x="160" y="103" text-anchor="middle" font-size="12" fill="currentColor">2. Salt и SRP_B</text>

  <!-- Step 3: Client -> Server -->
  <line x1="90" y1="145" x2="222" y2="145" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="230,145 222,141 222,149" fill="currentColor"/>
  <text x="160" y="138" text-anchor="middle" font-size="12" fill="currentColor">3. HKDF подпись</text>

  <!-- Step 4: Server -> Client -->
  <line x1="230" y1="180" x2="98" y2="180" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="90,180 98,176 98,184" fill="currentColor"/>
  <text x="160" y="173" text-anchor="middle" font-size="12" fill="currentColor">4. Токены JWT</text>"""
    },

    # 12. Gateway Fan-Out Architecture: ALB & API Gateway
    "ru/11.html": {
        "num": 12,
        "title": "Сетевая интеграция: авторизаторы API Gateway, правила ALB и микросервисы.",
        "aria": "Схема веерной маршрутизации сетевых авторизаторов к микросервисам",
        "h": 230,
        "content": """  <!-- Top: Ingress Request -->
  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">HTTPS Запрос (Access Token)</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <!-- Middle Authorizer Layer -->
  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Сетевой Authorizer (API GW / ALB)</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Валидация подписи JWKS и скоупов</text>

  <!-- Fan-Out to 3 Services -->
  <line x1="59" y1="88" x2="59" y2="114" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="59,120 55,112 63,112" fill="currentColor"/>

  <line x1="160" y1="88" x2="160" y2="114" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,120 156,112 164,112" fill="currentColor"/>

  <line x1="261" y1="88" x2="261" y2="114" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="261,120 257,112 265,112" fill="currentColor"/>

  <!-- 3 Microservices -->
  <rect x="12" y="120" width="94" height="42" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="59" y="137" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Lambda</text>
  <text x="59" y="151" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Хуки</text>

  <rect x="113" y="120" width="94" height="42" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="137" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">ECS</text>
  <text x="160" y="151" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Контейнеры</text>

  <rect x="214" y="120" width="94" height="42" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="261" y="137" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">EKS</text>
  <text x="261" y="151" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Pod Ingress</text>

  <!-- Summary Banner -->
  <line x1="160" y1="162" x2="160" y2="178" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,184 156,176 164,176" fill="currentColor"/>

  <rect x="20" y="184" width="280" height="30" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="202" text-anchor="middle" font-size="12" fill="currentColor">Заголовок X-Amzn-Oidc-Data</text>"""
    },

    # 13. Protocol Sequence Ladder: Custom Auth FIDO2 Passkeys
    "ru/12.html": {
        "num": 13,
        "title": "Системные потоки IGL: Passkeys FIDO2, Custom Auth и миграция пользователей.",
        "aria": "Схема беспарольного входа FIDO2 Passkeys в виде диаграммы обмена",
        "h": 220,
        "content": """  <!-- Left Column: User Device -->
  <rect x="10" y="15" width="80" height="190" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="50" y="34" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Клиент</text>
  <text x="50" y="48" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Passkey</text>

  <!-- Right Column: Custom Auth Engine -->
  <rect x="230" y="15" width="80" height="190" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="270" y="34" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Cognito</text>
  <text x="270" y="48" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Lambda</text>

  <!-- Step 1: User -> Server -->
  <line x1="90" y1="75" x2="222" y2="75" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="230,75 222,71 222,79" fill="currentColor"/>
  <text x="160" y="68" text-anchor="middle" font-size="12" fill="currentColor">1. DEFINE челлендж</text>

  <!-- Step 2: Server -> User -->
  <line x1="230" y1="110" x2="98" y2="110" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="90,110 98,106 98,114" fill="currentColor"/>
  <text x="160" y="103" text-anchor="middle" font-size="12" fill="currentColor">2. WebAuthn Nonce</text>

  <!-- Step 3: User -> Server -->
  <line x1="90" y1="145" x2="222" y2="145" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="230,145 222,141 222,149" fill="currentColor"/>
  <text x="160" y="138" text-anchor="middle" font-size="12" fill="currentColor">3. VERIFY подпись</text>

  <!-- Step 4: Server -> User -->
  <line x1="230" y1="180" x2="98" y2="180" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="90,180 98,176 98,184" fill="currentColor"/>
  <text x="160" y="173" text-anchor="middle" font-size="12" fill="currentColor">4. Успех сессии</text>"""
    },

    # 14. Progressive Stepping Stones: Noob Assessment Map
    "ru/13.html": {
        "num": 14,
        "title": "Структура квалификационного ассессмента Noob: карта 50 вопросов.",
        "aria": "Схема дорожной карты 5 блоков квалификации уровня Noob",
        "h": 230,
        "content": """  <!-- Stepping Stones Row 1 -->
  <rect x="15" y="10" width="135" height="34" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="82" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">User Pools (1-10)</text>
  <text x="82" y="38" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Каталог</text>

  <line x1="150" y1="27" x2="162" y2="27" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="170,27 162,23 162,31" fill="currentColor"/>

  <rect x="170" y="10" width="135" height="34" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="237" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">JWT Токены (11-20)</text>
  <text x="237" y="38" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Триада и JWKS</text>

  <!-- Stepping Stones Row 2 -->
  <rect x="15" y="68" width="135" height="34" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="82" y="84" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">OAuth PKCE (21-30)</text>
  <text x="82" y="96" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Клиенты SPA</text>

  <line x1="150" y1="85" x2="162" y2="85" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="170,85 162,81 162,89" fill="currentColor"/>

  <rect x="170" y="68" width="135" height="34" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="237" y="84" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Hosted UI (31-40)</text>
  <text x="237" y="96" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Вход и домены</text>

  <!-- Stepping Stone 5 (Center) -->
  <line x1="82" y1="102" x2="82" y2="120" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="82,126 78,118 86,118" fill="currentColor"/>

  <rect x="15" y="126" width="290" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="142" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">5. Базовый API (41-50)</text>
  <text x="160" y="154" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Защита от перечисления</text>

  <!-- Final Goal -->
  <line x1="160" y1="160" x2="160" y2="178" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,184 156,176 164,176" fill="currentColor"/>

  <rect x="20" y="184" width="280" height="30" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="202" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Квалификация: Инженер Noob</text>"""
    },

    # 15. 2x2 Grid with Central Integration Hub: Pro Assessment
    "ru/14.html": {
        "num": 15,
        "title": "Структура квалификационного ассессмента Pro: карта 50 вопросов.",
        "aria": "Схема инженерной матрицы 2х2 для квалификации уровня Pro",
        "h": 230,
        "content": """  <!-- 2x2 Grid Row 1 -->
  <rect x="15" y="8" width="135" height="40" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="82" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Триггеры (1-10)</text>
  <text x="82" y="38" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Pre Token &amp; Claims</text>

  <rect x="170" y="8" width="135" height="40" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="237" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">IdP (11-20)</text>
  <text x="237" y="38" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">SAML 2.0 &amp; OIDC</text>

  <!-- Connectors Row 1 to Row 2 -->
  <line x1="82" y1="48" x2="82" y2="58" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="82,66 78,58 86,58" fill="currentColor"/>

  <line x1="237" y1="48" x2="237" y2="58" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="237,66 233,58 241,58" fill="currentColor"/>

  <!-- 2x2 Grid Row 2 -->
  <rect x="15" y="66" width="135" height="40" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="82" y="82" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">STS Роли (21-30)</text>
  <text x="82" y="96" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Identity Pools</text>

  <rect x="170" y="66" width="135" height="40" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="237" y="82" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Защита (31-40)</text>
  <text x="237" y="96" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">WAFv2 &amp; ASF</text>

  <!-- Connectors to Pro Hub -->
  <line x1="82" y1="106" x2="82" y2="116" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="82,124 78,116 86,116" fill="currentColor"/>

  <line x1="237" y1="106" x2="237" y2="116" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="237,124 233,116 241,116" fill="currentColor"/>

  <!-- Block 5 + Pro Hub Banner -->
  <rect x="20" y="124" width="280" height="40" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="141" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">5. Terraform IaC (41-50)</text>
  <text x="160" y="155" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Интеграция с ALB и API Gateway</text>

  <!-- Connector Pro Hub to Qualification Banner -->
  <line x1="160" y1="164" x2="160" y2="176" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,184 156,176 164,176" fill="currentColor"/>

  <rect x="40" y="184" width="240" height="28" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="202" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Квалификация: Инженер Pro</text>"""
    },

    # 16. Multi-Region Active-Active Mesh: IGL Architecture
    "ru/15.html": {
        "num": 16,
        "title": "Структура квалификационного ассессмента IGL: карта 50 архитектурных кейсов.",
        "aria": "Схема мультирегиональной репликации актив-актив уровня IGL",
        "h": 230,
        "content": """  <!-- Primary Region -->
  <rect x="20" y="10" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Регион us-east-1 (Primary)</text>
  <text x="160" y="38" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">User Pool A • Hosted UI • Route 53</text>

  <!-- Bidirectional Event Sync -->
  <line x1="85" y1="44" x2="85" y2="66" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,74 81,66 89,66" fill="currentColor"/>

  <line x1="235" y1="44" x2="235" y2="66" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,74 231,66 239,66" fill="currentColor"/>

  <!-- Sync Engine -->
  <rect x="15" y="74" width="140" height="42" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="93" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">DynamoDB Global</text>
  <text x="85" y="107" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Асинхронная репликация</text>

  <rect x="165" y="74" width="140" height="42" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="93" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Replicator</text>
  <text x="235" y="107" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Синхронизация паролей</text>

  <!-- Secondary Region -->
  <line x1="85" y1="116" x2="85" y2="132" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,140 81,132 89,132" fill="currentColor"/>

  <line x1="235" y1="116" x2="235" y2="132" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,140 231,132 239,132" fill="currentColor"/>

  <rect x="20" y="140" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="156" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Регион eu-west-1 (Secondary)</text>
  <text x="160" y="168" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">User Pool B • Автоматический фейловер</text>

  <!-- Bottom IGL Target -->
  <rect x="30" y="186" width="260" height="28" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="204" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Zero-RTO Архитектура IGL</text>"""
    },

    # 17. 3x3 Radial Lens Matrix: Navigator
    "ru/navigator.html": {
        "num": 17,
        "title": "Матрица девяти инженерных линз вокруг ядра Amazon Cognito.",
        "aria": "Схема 3х3 аналитической матрицы девяти инженерных линз",
        "h": 240,
        "content": """  <!-- Row 1: Core Architecture Lenses -->
  <rect x="15" y="8" width="90" height="32" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="60" y="28" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">1. Components</text>

  <rect x="115" y="8" width="90" height="32" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="28" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">2. Code &amp; IaC</text>

  <rect x="215" y="8" width="90" height="32" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="260" y="28" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">3. Strength</text>

  <!-- Connectors from Row 1 to Hub -->
  <line x1="60" y1="40" x2="60" y2="52" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="60,60 56,52 64,52" fill="currentColor"/>

  <line x1="160" y1="40" x2="160" y2="52" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,60 156,52 164,52" fill="currentColor"/>

  <line x1="260" y1="40" x2="260" y2="52" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="260,60 256,52 264,52" fill="currentColor"/>

  <!-- Center Hub: Amazon Cognito Matrix -->
  <rect x="20" y="60" width="280" height="38" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="77" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Ядро сервиса: Amazon Cognito</text>
  <text x="160" y="91" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Синтез по 9 линзам</text>

  <!-- Connectors from Hub to Row 2 -->
  <line x1="60" y1="98" x2="60" y2="110" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="60,118 56,110 64,110" fill="currentColor"/>

  <line x1="160" y1="98" x2="160" y2="110" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,118 156,110 164,110" fill="currentColor"/>

  <line x1="260" y1="98" x2="260" y2="110" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="260,118 256,110 264,110" fill="currentColor"/>

  <!-- Row 2: Ecosystem Lenses -->
  <rect x="15" y="118" width="90" height="32" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="60" y="138" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">4. Limits</text>

  <rect x="115" y="118" width="90" height="32" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="138" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Ecosystem</text>

  <rect x="215" y="118" width="90" height="32" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="260" y="138" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">AI Context</text>

  <!-- Connectors from Row 2 to Row 3 -->
  <line x1="60" y1="150" x2="60" y2="166" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="60,174 56,166 64,166" fill="currentColor"/>

  <line x1="160" y1="150" x2="160" y2="166" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,174 156,166 164,166" fill="currentColor"/>

  <line x1="260" y1="150" x2="260" y2="166" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="260,174 256,166 264,166" fill="currentColor"/>

  <!-- Row 3: Operational Lenses -->
  <rect x="15" y="174" width="90" height="32" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="60" y="194" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">7. Cloud</text>

  <rect x="115" y="174" width="90" height="32" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="194" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">8. DevOps</text>

  <rect x="215" y="174" width="90" height="32" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="260" y="194" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">9. SRE</text>"""
    }
}

def inject():
    import re
    for fpath, meta in DIAGRAMS.items():
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # Remove existing figure box if present
        pattern = re.compile(r'\s*<div class="box figure">.*?</div>\s*', re.DOTALL)
        html = pattern.sub('\n', html)

        fig = f"""
    <div class="box figure">
      <svg viewBox="0 0 320 {meta['h']}" style="max-width:320px;height:auto;display:block;margin:0 auto" role="img" aria-label="{meta['aria']}">
{meta['content']}
      </svg>
      <p class="dim">Схема {meta['num']}. {meta['title']}</p>
    </div>"""

        pos = html.find('id="key-idea"')
        if pos == -1:
            raise RuntimeError(f"id=\"key-idea\" not found in {fpath}")

        close_div = html.find('</div>', pos)
        if close_div == -1:
            raise RuntimeError(f"Closing </div> not found for key-idea in {fpath}")

        new_html = html[:close_div] + fig + "\n    " + html[close_div:]
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_html)

        print(f"Updated Scheme {meta['num']} in {fpath}")

if __name__ == "__main__":
    inject()
