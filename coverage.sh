omit="*yaml*","*test_*","*__init__.py"
options="-a --omit=$omit -m"
coverage erase
coverage run $options engine.test.test_app
coverage run $options engine.test.test_battle_logger
coverage run $options engine.test.test_battle
coverage run $options engine.test.test_dice
coverage run $options engine.test.test_entity_def
coverage run $options engine.test.test_entity
coverage run $options engine.test.test_force
coverage run $options engine.test.test_util
coverage html
coverage xml