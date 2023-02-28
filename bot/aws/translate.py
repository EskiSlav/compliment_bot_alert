from __future__ import annotations

import boto3


class Translator:
    def __init__(self) -> None:
        self.translate = boto3.client(
            service_name='translate', region_name='eu-west-2',
        )

    def translate_text(self, text, from_lang='en', to_lang='uk'):
        result = self.translate.translate_text(
            Text=text, SourceLanguageCode=from_lang,
            TargetLanguageCode=to_lang,
        )
        return result.get('TranslatedText')
