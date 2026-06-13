ARGUMENT_TEST_CASES = [

    {
        "question": "restart nginx container",
        "tool_name": "restart_container",
        "expected_args": {
            "container_identifier": "nginx"
        }
    },

    {
        "question": "show logs of nginx container",
        "tool_name": "docker_logs",
        "expected_args": {
            "container_identifier": "nginx"
        }
    },

    {
        "question": "describe pod frontend",
        "tool_name": "describe_pod",
        "expected_args": {
            "pod_name": "frontend"
        }
    },

    {
        "question": "show logs of payment-service pod",
        "tool_name": "pod_logs",
        "expected_args": {
            "pod_name": "payment-service"
        }
    },

    {
        "question": "describe deployment backend",
        "tool_name": "describe_deployment",
        "expected_args": {
            "deployment_name": "backend"
        }
    }

]