# Databricks notebook source
# MAGIC %md
# MAGIC # Register UC Functions for AI tools
# MAGIC

# COMMAND ----------

# MAGIC %pip install -r ../../requirements.txt -q

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

import sys


dbutils.widgets.text("root_path", "")
dbutils.widgets.text("env", "dev")
dbutils.widgets.text("git_commit", "")
dbutils.widgets.text("agent_catalog", "telco_customer_support_dev")
dbutils.widgets.text("data_catalog", "telco_customer_support_dev")
dbutils.widgets.text("agent_schema", "agent")
dbutils.widgets.text("data_schema", "gold")
dbutils.widgets.text("model_name", "telco_customer_support_agent")
dbutils.widgets.text("experiment_name", "/Shared/telco_support_agent/dev/dev_telco_support_agent")
dbutils.widgets.text("disable_tools", "")


# COMMAND ----------

if root_path := dbutils.widgets.get("root_path"):
    sys.path.append(root_path)

# COMMAND ----------

from telco_support_agent.config import UCConfig
from telco_support_agent.tools.billing.functions import register_get_billing_info, register_get_usage_info
from telco_support_agent.tools.account.functions import register_customer_info, register_customer_subscriptions
from telco_support_agent.tools.product.functions import register_customer_devices_info, register_devices_info, register_plans_info, register_promos_info


# COMMAND ----------
# Load UC config from widgets
uc_config = UCConfig(
    data_catalog=dbutils.widgets.get("data_catalog"),
    agent_catalog=dbutils.widgets.get("agent_catalog"),
    agent_schema=dbutils.widgets.get("agent_schema"),
    data_schema=dbutils.widgets.get("data_schema"),
    model_name=dbutils.widgets.get("model_name"),
)

# COMMAND ----------
# Register UC functions
register_get_billing_info(uc_config)
register_get_usage_info(uc_config)

# COMMAND ----------
# Register UC functions
register_customer_info(uc_config)
register_customer_subscriptions(uc_config)

# COMMAND ----------
register_customer_devices_info(uc_config)
register_devices_info(uc_config)
register_plans_info(uc_config)
register_promos_info(uc_config)
