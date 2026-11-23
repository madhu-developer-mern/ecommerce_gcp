from django.db import models

# In SimpleShop, the active shopping cart is maintained client-side in React Context
# and localStorage for responsive UX, simple deployment, and stateless server readiness.
# Orders are finalized through the /api/orders/ endpoint.
