omit="*yaml*","*test_*","*__init__.py"
coverage erase
coverage run -m -a --omit=$omit engine.test.test_app
coverage run -m -a --omit=$omit engine.test.test_battle_logger
#coverage run -m -a --omit=$omit engine.test.test_battle
coverage run -m -a --omit=$omit engine.test.test_dice
coverage run -m -a --omit=$omit engine.test.test_entity_def
coverage run -m -a --omit=$omit engine.test.test_entity
coverage run -m -a --omit=$omit engine.test.test_force
coverage run -m -a --omit=$omit engine.test.test_util
coverage html
coverage xml