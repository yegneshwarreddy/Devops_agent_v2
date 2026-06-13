PLANNER_TEST_CASES = [

    {
        "question": "show running containers",
        "expected_tool": "docker_ps"
    },

    {
        "question": "restart nginx container",
        "expected_tool": "restart_container"
    },

    {
        "question": "show docker images",
        "expected_tool": "docker_images"
    },

    {
        "question": "describe pod frontend",
        "expected_tool": "describe_pod"
    },

    {
        "question": "show logs of frontend pod",
        "expected_tool": "pod_logs"
    }

]