# -*- coding: utf-8 -*-

"""Classes for CloudFront Distributions."""


class DistributionManager:
    """Manage CloudFront distributions."""

    def __init__(self, session):
        """Create a DistributionManager."""
        self.session = session
        self.client = self.session.client('cloudfront')

    def find_matching_dist(self, domain_name):
        """Find a dist matching domain_name."""
        distributions = self.client.list_distributions()
        if distributions['DistributionList']['Quantity'] > 0:
            for dist in distributions['DistributionList']['Items']:
                dist_name = dist['DomainName']
                print("Name: " + dist_name)
                if dist_name == domain_name:
                    return True
                    if dist_name[0] == '*' and \
                            domain_name.endswith(dist_name[1:]):
                        return True
            return False
        else:
            print("Error: No CloudFront distributions detected.")

    def create_dist(self, domain_name, cert):
        """Create a dist for domain_name using cert."""
        pass

    def await_deploy(self, dist):
        """Wait for dist to be deployed."""
        pass
