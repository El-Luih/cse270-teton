import pytest
import json
from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                              get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures)
 
def test_get_seven_letter_word(mocker):
    mocker.patch("builtins.input", return_value="abcdefg")
    result = get_seven_letter_word()
    assert result == "ABCDEFG"
 
    mocker.patch("builtins.input", return_value="abc")
    with pytest.raises(ValueError):
        get_seven_letter_word()
 
def test_parse_json_from_file(tmp_path):
    data = {"adjectives": ["big", "small"], "nouns": ["cat", "dog"]}
    file_path = tmp_path / "test_words.json"
    file_path.write_text(json.dumps(data))
    result = parse_json_from_file(file_path)
    assert result == data
 
def test_choose_sentence_structure():
    result = choose_sentence_structure()
    assert result in structures
 
def test_get_pronoun():
    pronouns = ["he", "she", "they", "I", "we"]
    result = get_pronoun()
    assert result in pronouns
 
def test_get_article():
    articles = ["a", "the"]
    result = get_article()
    assert result in articles
 
def test_get_word():
    word_list = ["apple", "banana", "cherry"]
    result = get_word("A", word_list)
    assert result == "apple"
 
def test_fix_agreement():
    # Covers lines 63, 69: he/she rule and a->an rule
    sentence = ["he", "quickly", "run", "a", "old", "apple"]
    fix_agreement(sentence)
    assert sentence[2] == "runs"
    assert sentence[3] == "an"
 
    # Covers line 72: 'the' at index 0 adds s to verb
    sentence2 = ["the", "big", "cat", "slowly", "run", "over", "the", "small", "dog"]
    fix_agreement(sentence2)
    assert sentence2[4] == "runs"
 
def test_build_sentence(mocker):
    mocker.patch("random.choice", side_effect=lambda x: x[0])
    data = {
        "adjectives":   ["big",   "small",  "tall",  "fast",  "cold",  "dark",  "loud"],
        "nouns":        ["cat",   "dog",    "bird",  "fish",  "frog",  "wolf",  "bear"],
        "verbs":        ["run",   "jump",   "swim",  "fly",   "crawl", "walk",  "sit"],
        "adverbs":      ["fast",  "slow",   "high",  "near",  "low",   "far",   "hard"],
        "prepositions": ["over",  "under",  "near",  "past",  "by",    "from",  "into"]
    }
    # structures[0] has no PRO - covers ART/ADJ/NOUN/ADV/VERB/PREP branches
    result = build_sentence("ABCDEFG", structures[0], data)
    assert isinstance(result, str)
    assert result[0].isupper()
 
    # structures[1] has PRO - covers lines 96-97
    result2 = build_sentence("ABCDEFG", structures[1], data)
    assert isinstance(result2, str)
    assert result2[0].isupper()
 