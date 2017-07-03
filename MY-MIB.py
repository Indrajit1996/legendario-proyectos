# PySNMP SMI module. Autogenerated from smidump -f python MY-MIB
# by libsmi2pysnmp-0.1.3 at Wed Nov  9 11:17:40 2016,
# Python version sys.version_info(major=2, minor=7, micro=6, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, Integer32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, enterprises, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "enterprises")

# Objects

myCompany = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
testCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: testCount.setDescription("A sample count of something.")
testDescription = MibScalar((1, 3, 6, 1, 4, 1, 42, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: testDescription.setDescription("A description of something")
testInteger = MibScalar((1, 3, 6, 1, 4, 1, 42, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: testInteger.setDescription("A sample Integer.")

# Augmentions

# Notifications

testTrap = NotificationType((1, 3, 6, 1, 4, 1, 42, 3)).setObjects(*() )
if mibBuilder.loadTexts: testTrap.setDescription("Test notification")

# Exports

# Objects
mibBuilder.exportSymbols("MY-MIB", myCompany=myCompany, testCount=testCount, testDescription=testDescription, testInteger=testInteger)

# Notifications
mibBuilder.exportSymbols("MY-MIB", testTrap=testTrap)

