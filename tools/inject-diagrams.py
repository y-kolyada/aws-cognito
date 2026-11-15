#!/usr/bin/env python3
"""Inject 17 inline SVG diagrams into course pages."""

import os
import re

DIAGRAMS = {
    "ru/index.html": {
        "num": 1,
        "title": "Архитектурная модель сервиса: User Pools (каталог и токены) против Identity Pools (роли STS).",
        "aria": "Схема архитектурной модели Cognito: разделение User Pools и Identity Pools",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Клиент (Web / Mobile)</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Cognito User Pool (Каталог &amp; IdP)</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Аутентификация • Токены JWT</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Бэкенд API</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">JWT Authorizer</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Identity Pool</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Федерация STS</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Микросервисы</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">ALB • ECS • Lambda</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Сервисы AWS</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">S3 • DynamoDB (SigV4)</text>"""
    },

    "ru/01.html": {
        "num": 2,
        "title": "Анатомия каталога User Pool: структура атрибутов, политики паролей и верификация.",
        "aria": "Схема анатомии каталога User Pool: структура атрибутов, политики паролей и верификация",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Клиент (SignUp / SignIn)</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Каталог Amazon Cognito User Pool</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Схема атрибутов • Политика паролей</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Верификация OTP</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Email / SMS код</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Безопасность</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">MFA • SRP вход</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">CONFIRMED</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Активация профиля</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Выдача сессии</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">OIDC токены каталога</text>"""
    },

    "ru/02.html": {
        "num": 3,
        "title": "Триада токенов OIDC и OAuth 2.0: ID, Access, Refresh и проверка JWKS.",
        "aria": "Схема триады токенов OIDC: ID, Access, Refresh и криптографическая проверка JWKS",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Cognito IdP (/oauth2/token)</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Клиентское приложение (SPA / App)</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">ID Token • Access Token • Refresh Token</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">API Gateway</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Access Token</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">JWKS Endpoint</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Ключи RSA (JWKS)</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Бэкенд сервис</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Доступ разрешен</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Ротация токенов</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Refresh Token Flow</text>"""
    },

    "ru/03.html": {
        "num": 4,
        "title": "Поток Authorization Code с криптографическим протоколом PKCE.",
        "aria": "Схема протокола OAuth 2.0 Authorization Code с криптографической защитой PKCE",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Клиент (code_verifier + hash)</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Cognito /oauth2/authorize</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Вход • Редирект с auth code</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Обмен кода</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">/oauth2/token</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Проверка PKCE</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">SHA256(verifier)</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Выдача токенов</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">ID, Access, Refresh</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Защита от кражи</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Безопасность SPA</text>"""
    },

    "ru/04.html": {
        "num": 5,
        "title": "Топология Hosted UI: CloudFront, ACM в us-east-1 и кастомный домен.",
        "aria": "Схема топологии Cognito Hosted UI: кастомный домен, CloudFront и ACM сертификат",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Пользовательский браузер</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Amazon CloudFront (Hosted UI Edge)</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">auth.example.com • ACM us-east-1</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Брендинг UI</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Логотип &amp; CSS</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">User Pool Core</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Каталог &amp; Сессия</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Redirect URI</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Коллбэк в SPA</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Выдача Code</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Авторизация</text>"""
    },

    "ru/05.html": {
        "num": 6,
        "title": "Корпоративная и социальная федерация: интеграция SAML 2.0 и OIDC с JIT.",
        "aria": "Схема внешней федерации: интеграция SAML 2.0 и OIDC с Just-In-Time провижинингом",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Внешний IdP (Okta / Google)</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Cognito Federation Broker</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">SAML 2.0 Assertion • OIDC Tokens</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Маппинг claims</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Claims -> User Pool</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">JIT-провижининг</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Создание профиля</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Связывание</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">AdminLinkProvider</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Локальный JWT</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Единый формат токенов</text>"""
    },

    "ru/06.html": {
        "num": 7,
        "title": "Жизненный цикл бессерверных триггеров AWS Lambda в User Pool.",
        "aria": "Схема жизненного цикла бессерверных триггеров AWS Lambda в Amazon Cognito",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">События Cognito User Pool</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Шина триггеров AWS Lambda</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Синхронные хуки • Таймаут 5 сек</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Pre Sign-up</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Валидация email</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Pre Token Gen</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Обогащение claims</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Post Confirmation</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Запись в DynamoDB</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Custom Message</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Шаблоны уведомлений</text>"""
    },

    "ru/07.html": {
        "num": 8,
        "title": "Обмен токенов на временные учетные данные AWS STS через Identity Pool.",
        "aria": "Схема обмена токенов User Pool на временные ключи AWS STS через Identity Pool",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Клиент (User Pool ID Token)</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Cognito Identity Pool</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">GetId • GetCredentialsForIdentity</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Auth Role</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Роль логина</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Unauth Role</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Гостевая роль</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">AWS STS Сервис</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">STS AssumeRole</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Ключи SigV4</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Прямой доступ к S3</text>"""
    },

    "ru/08.html": {
        "num": 9,
        "title": "Эшелонированная защита каталога: интеграция AWS WAFv2 и Cognito ASF.",
        "aria": "Схема эшелонированной защиты каталога: интеграция AWS WAFv2 и Cognito Advanced Security",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Входящий интернет-трафик</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">AWS WAFv2 Web ACL</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Bot Control • Ограничение частоты</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Cognito ASF</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Адаптивный риск</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Утечки паролей</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Compromised Creds</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Действие: MFA</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Запрос подтверждения</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Действие: Блок</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Отказ входа</text>"""
    },

    "ru/09.html": {
        "num": 10,
        "title": "Модель тарификации MAU, защита от SMS Toll Fraud и квоты API.",
        "aria": "Схема экономики сервиса: тарификация MAU, защита от SMS Toll Fraud и квоты API",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">База пользователей каталога</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Тарификация MAU (Monthly Active)</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">50 000 Free Tier • Ступени цены</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">SMS Toll Fraud</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Защита от фрода</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Квоты API IdP</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Лимиты TPS и Burst</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Отказ от SMS</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">TOTP токены</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Кэш сессий</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Снижение вызовов API</text>"""
    },

    "ru/10.html": {
        "num": 11,
        "title": "Базовая инфраструктура User Pool в Terraform и SRP-аутентификация.",
        "aria": "Схема инфраструктуры User Pool в Terraform и криптографический протокол SRP",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Terraform: User Pool IaC</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">USER_SRP_AUTH (SRP-6a)</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Аутентификация без передачи пароля</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">InitiateAuth</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Передача SRP_A</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Auth Challenge</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">SRP Verifier</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">HKDF сигнатура</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Ответ клиента</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Успех сессии</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Выдача токенов</text>"""
    },

    "ru/11.html": {
        "num": 12,
        "title": "Сетевая интеграция: авторизаторы API Gateway, правила ALB и микросервисы.",
        "aria": "Схема сетевой интеграции: авторизаторы API Gateway, правила ALB и микросервисы",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Клиентский запрос (HTTPS Bearer)</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Сетевые шлюзы API Gateway / ALB</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Cognito Authorizer • Проверка JWKS</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">ALB Authenticate</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">OIDC редирект</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">JWT Authorizer</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">HTTP API Gateway</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Заголовок claims</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">X-Amzn-Oidc-Data</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Микросервисы</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">ECS • Lambda • EKS</text>"""
    },

    "ru/12.html": {
        "num": 13,
        "title": "Системные потоки IGL: Passkeys FIDO2, Custom Auth и миграция пользователей.",
        "aria": "Схема системных потоков IGL: Passkeys FIDO2, Custom Auth и миграция пользователей",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Пользователь (Passkey / WebAuthn)</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Cognito Custom Auth Flow</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Define / Create / Verify Challenge</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Passkeys FIDO2</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Аппаратный ключ</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">User Migration</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Миграция на лету</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Zero-Password</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Биометрия клиента</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Legacy БД</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Перенос данных</text>"""
    },

    "ru/13.html": {
        "num": 14,
        "title": "Структура квалификационного ассессмента Noob: карта 50 вопросов.",
        "aria": "Схема квалификационного ассессмента Noob: структура 50 вопросов",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Ассессмент Noob (50 вопросов)</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Фундаментальные концепции CIAM</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Каталоги • Токены • OAuth 2.0 • Вход</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Блок 1 (1-10)</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">User Pools каталог</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Блок 2 (11-20)</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">JWT токены и JWKS</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Блок 3 (21-30)</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">OAuth 2.0 и PKCE</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Блоки 4-5 (31-50)</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Hosted UI и базовый API</text>"""
    },

    "ru/14.html": {
        "num": 15,
        "title": "Структура квалификационного ассессмента Pro: карта 50 вопросов.",
        "aria": "Схема квалификационного ассессмента Pro: структура 50 вопросов промышленной практики",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Ассессмент Pro (50 вопросов)</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Промышленная инженерия CIAM</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Триггеры • STS • WAF • Terraform</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Блок 1 (1-10)</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Lambda хуки</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Блок 2 (11-20)</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">SAML 2.0 и OIDC IdP</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Блок 3 (21-30)</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Identity Pools &amp; STS</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Блоки 4-5 (31-50)</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">WAFv2 и IaC</text>"""
    },

    "ru/15.html": {
        "num": 16,
        "title": "Структура квалификационного ассессмента IGL: карта 50 архитектурных кейсов.",
        "aria": "Схема квалификационного ассессмента IGL: структура 50 архитектурных кейсов",
        "h": 230,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Ассессмент IGL (50 кейсов)</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Архитектурные решения Lead</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Мультирегион • Zero-Downtime • FinOps</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Блок 1 (1-10)</text>
  <text x="85" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Мультирегион</text>

  <rect x="165" y="120" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Блок 2 (11-20)</text>
  <text x="235" y="148" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Zero-Downtime</text>

  <line x1="85" y1="156" x2="85" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,180 81,172 89,172" fill="currentColor"/>

  <line x1="235" y1="156" x2="235" y2="174" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,180 231,172 239,172" fill="currentColor"/>

  <rect x="15" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Блок 3 (21-30)</text>
  <text x="85" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">FIDO2 passkeys</text>

  <rect x="165" y="180" width="140" height="36" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Блоки 4-5 (31-50)</text>
  <text x="235" y="208" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">FinOps и SRE</text>"""
    },

    "ru/navigator.html": {
        "num": 17,
        "title": "Матрица девяти инженерных линз вокруг ядра Amazon Cognito.",
        "aria": "Схема матрицы девяти инженерных линз вокруг ядра архитектуры Amazon Cognito",
        "h": 240,
        "content": """  <rect x="40" y="8" width="240" height="26" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="25" text-anchor="middle" font-size="12" fill="currentColor">Инженерный навигатор курса</text>

  <line x1="160" y1="34" x2="160" y2="48" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="160,54 156,46 164,46" fill="currentColor"/>

  <rect x="20" y="54" width="280" height="34" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="160" y="69" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Ядро сервиса: Amazon Cognito</text>
  <text x="160" y="82" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Матрица девяти сквозных инженерных линз</text>

  <path d="M 160 88 L 160 102 L 85 102 L 85 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,120 81,112 89,112" fill="currentColor"/>

  <path d="M 160 88 L 160 102 L 235 102 L 235 114" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,120 231,112 239,112" fill="currentColor"/>

  <rect x="15" y="120" width="140" height="38" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Архитектура</text>
  <text x="85" y="150" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Компоненты • Сила</text>

  <rect x="165" y="120" width="140" height="38" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="235" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Экосистема</text>
  <text x="235" y="150" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Лимиты • ИИ</text>

  <line x1="85" y1="158" x2="85" y2="178" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="85,184 81,176 89,176" fill="currentColor"/>

  <line x1="235" y1="158" x2="235" y2="178" stroke="currentColor" stroke-width="1.4"/>
  <polygon points="235,184 231,176 239,176" fill="currentColor"/>

  <rect x="15" y="184" width="140" height="38" rx="4" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="1.2"/>
  <text x="85" y="199" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Эксплуатация</text>
  <text x="85" y="214" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Облако • DevOps</text>

  <rect x="165" y="184" width="140" height="38" rx="4" fill="currentColor" fill-opacity="0.08" stroke="var(--acc, #0284c7)" stroke-width="1.4"/>
  <text x="235" y="199" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Сквозной синтез</text>
  <text x="235" y="214" text-anchor="middle" font-size="12" opacity="0.8" fill="currentColor">Главы 01-15 • SRE</text>"""
    }
}

def inject():
    for fpath, meta in DIAGRAMS.items():
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # Check if already injected
        if '<div class="box figure">' in html:
            # Replace existing figure box
            pattern = re.compile(r'\s*<div class="box figure">.*?</div>\s*', re.DOTALL)
            html = pattern.sub('\n', html)

        fig = f"""
    <div class="box figure">
      <svg viewBox="0 0 320 {meta['h']}" style="max-width:320px;height:auto;display:block;margin:0 auto" role="img" aria-label="{meta['aria']}">
{meta['content']}
      </svg>
      <p class="dim">Схема {meta['num']}. {meta['title']}</p>
    </div>"""

        # Find closing tag of key-idea box
        # Search for `<div class="box key" id="key-idea">`
        pos = html.find('id="key-idea"')
        if pos == -1:
            raise RuntimeError(f"id=\"key-idea\" not found in {fpath}")

        # Find the closing </div> of this box
        # After key-idea, find the next `</div>`
        close_div = html.find('</div>', pos)
        if close_div == -1:
            raise RuntimeError(f"Closing </div> not found for key-idea in {fpath}")

        new_html = html[:close_div] + fig + "\n    " + html[close_div:]
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_html)

        print(f"Injected Scheme {meta['num']} into {fpath}")

if __name__ == "__main__":
    inject()
