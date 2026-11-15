# Diagram sources

A diagram on a page is **inline SVG**, not an image file: the page must work from `file://`, and inline vector inherits the theme colour through `currentColor`, so it survives the day/night switch without a second copy. A shared `assets/NN.svg` would also show one language's labels on all four language pages. The full rule is `AGENTS.md` section 5 rule 18, and `node tools/check-diagrams.mjs` guards it.

This folder holds the **source** of each diagram in Mermaid: `NN-name.mmd`, where `NN` is the page the diagram lives on. Every source answers a diagram and every diagram answers a source; the check says so out loud when they drift apart.

**State the truth about the renderer here.** If no Mermaid renderer is installed, the SVG on the page is drawn by hand from this source rather than exported from it, and this file must say that plainly - otherwise the folder quietly becomes the lie "rendered from mermaid". When a renderer or a viewer appears, the `.mmd` becomes the master and the SVG the derivative.

| Source | Page | What it shows |
| :-- | :-- | :-- |
| `index-arch.mmd` | `ru/index.html` | Архитектурная модель сервиса: User Pools (каталог и токены) против Identity Pools (роли STS). |
| `01-user-pools.mmd` | `ru/01.html` | Анатомия каталога User Pool: структура атрибутов, политики паролей и верификация. |
| `02-jwt-triad.mmd` | `ru/02.html` | Триада токенов OIDC и OAuth 2.0: ID, Access, Refresh и криптографическая проверка через JWKS. |
| `03-oauth-pkce.mmd` | `ru/03.html` | Поток Authorization Code с криптографическим протоколом PKCE для публичных клиентов. |
| `04-hosted-ui.mmd` | `ru/04.html` | Топология Hosted UI: CloudFront, ACM-сертификат в us-east-1 и кастомный домен авторизации. |
| `05-federation-saml-oidc.mmd` | `ru/05.html` | Корпоративная и социальная федерация: интеграция SAML 2.0 и OIDC с JIT-провижинингом. |
| `06-lambda-triggers.mmd` | `ru/06.html` | Жизненный цикл бессерверных триггеров AWS Lambda в User Pool (Pre/Post хуки и обогащение токенов). |
| `07-identity-pools-sts.mmd` | `ru/07.html` | Обмен токенов на временные учетные данные AWS STS через Identity Pool для доступа к сервисам AWS. |
| `08-waf-advanced-security.mmd` | `ru/08.html` | Эшелонированная защита каталога: интеграция AWS WAFv2 и адаптивной риск-аутентификации ASF. |
| `09-economics-quotas.mmd` | `ru/09.html` | Экономика и масштабирование: модель MAU, защита от SMS Toll Fraud и лимиты API Identity Provider. |
| `10-noob-iac.mmd` | `ru/10.html` | Базовая инфраструктура User Pool в Terraform и протокол SRP-аутентификации без передачи пароля. |
| `11-pro-integrations.mmd` | `ru/11.html` | Сетевая интеграция: авторизаторы API Gateway, правила ALB и обогащение токенов Pre Token Generation. |
| `12-igl-architecture.mmd` | `ru/12.html` | Архитектурные потоки IGL: Passkeys FIDO2, беспарольный Custom Auth и фоновая миграция пользователей. |
| `13-assessment-noob.mmd` | `ru/13.html` | Структура квалификационного ассессмента Noob: карта 50 вопросов по фундаментальным концепциям. |
| `14-assessment-pro.mmd` | `ru/14.html` | Структура квалификационного ассессмента Pro: карта 50 вопросов по промышленной эксплуатации. |
| `15-assessment-igl.mmd` | `ru/15.html` | Структура квалификационного ассессмента IGL: карта 50 архитектурных кейсов высшего уровня. |
| `navigator-lenses.mmd` | `ru/navigator.html` | Матрица девяти сквозных инженерных линз вокруг ядра архитектуры Amazon Cognito. |
