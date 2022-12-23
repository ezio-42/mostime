from typing import List, Optional, Sequence, Tuple, TypeAlias

import arbitrary
import pytest
from arbitrary import arbitrary_string

TestData: TypeAlias = Tuple[str, int, Optional[str]]

# Existing endpoints and their test data
existing_endpoints_test_data = [
    ("/", 200, "Time in Moscow is 12:21:12"),
    ("/visits", 200, "Total visits"),
    ("/health", 200, "Up"),
]


# Generate test data for non existing endpoints
def not_found_endpoints(
    existing_endpoints_test_data: Sequence[TestData],
    n: int = 100,
) -> List[TestData]:
    """Generate test data for non existing endpoints."""
    existing_endpoints = set(
        map(
            lambda xs: xs[0],
            existing_endpoints_test_data,
        )
    )
    return [
        (s, 404, None)
        for s in arbitrary.not_in(arbitrary_string, existing_endpoints, n)
    ]


@pytest.mark.freeze_time("12:21:12", tz_offset=-3)  # freeze time to 12:21:12
@pytest.mark.parametrize(
    # test parametrized by endpoint, status and substr in response
    "endpoint, status, substr",
    [
        ("/", 200, "Time in Moscow is 12:21:12"),
        ("/visits", 200, "Total visits"),
        ("/health", 200, "Up"),
    ],
)
@pytest.mark.it("should return correct response")  # BDD style
async def test_existing_endpoints(endpoint, status, substr, api_client):
    """
    Test that existing endpoints return correct response.
    """
    resp = await api_client.get(endpoint)
    assert resp.status == status
    if substr is not None:
        assert substr in await resp.text()


# property based test
@pytest.mark.parametrize(
    "endpoint",
    not_found_endpoints(existing_endpoints_test_data),
)
@pytest.mark.it("should return 404")  # BDD style
async def test_property_non_existing_endpoints_always_return_404(
    endpoint: str,
    api_client,
):
    """Test that non existing endpoints always return 404."""
    resp = await api_client.get(f"/{endpoint}")
    assert resp.status == 404
