from envs.actions import decode_action, ACTION_BOUNDS


def test_action_clip():
    a = [100.0, -10.0, 5.0, 0.0, -1.0]
    policy_vars = decode_action(a)
    for x, (lo, hi) in zip(policy_vars, ACTION_BOUNDS):
        assert lo <= x <= hi
