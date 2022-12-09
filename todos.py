# blueprints: will need 6 diff tables.
# how to separate functionality?
# admin will need login security credentials. should also leave these credentials for employees..they will eventually login? or will they never need to use the portal? yes they will. to start no. maybe later. 
# admin will need confidential access to their accts to start.
# rest of the tables, equipment, order, bank_acct, order_equipment can all be in different folder: they are all related to employee fns, so maybe it could be /onboarding
# so ADMIN, EMPLOYEE in auth dir
# rest of classes in onboarding dir
# people will need authentication procedures. employee bank? leave simple for now.
# 