from jingo import register
from models import Translation

@register.function
def get_entry_translation(entry, locale):
    translation = entry.description
    if locale != 'en-US':
        try:
            translated_entry = entry.translation_set.get(language__language_code=locale)
            translation = translated_entry.translation
        except Translation.DoesNotExist:
            pass
    return translation
