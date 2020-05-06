mvn clean install

mvn clean install -fae -DskipMunitTests
  -fae : fail at end allows a build of the components that are passing.
  -DskipMunitTests : allows to skip the unit tests
