# sensu-plugins-rpm-spec

A boilerplate spec file for creating an RPM containing sensu plugins

# Why?

If you're using [sensu](https://sensuapp.org), you probably install a bunch of ruby based monitoring plugins to monitor things.

The issue with installing these plugins is that it can take a _long_ time to install all the dependencies. This RPM spec file does the hard work at build time, so installing sensu plugins is nice and quick.

# Considerations

This is designed as boilerplate. It will need to be modified to suit your needs.
