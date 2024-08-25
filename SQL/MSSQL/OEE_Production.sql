SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[OEE_Production](
	[ProductionId] [uniqueidentifier] NOT NULL,
	[BeginDateTime] [datetime] NOT NULL,
	[EndDateTime] [datetime] NULL,
	[ContextId] [uniqueidentifier] NULL,
	[GoodCount] [int] NULL,
	[BadCount] [int] NULL,
	[StopCount] [int] NULL,
	[DowntimeSeconds] [int] NULL,
	[RuntimeSeconds] [int] NULL
) ON [PRIMARY]
GO
CREATE CLUSTERED INDEX [IX_OEE_Production_BeginDateTime] ON [dbo].[OEE_Production]
(
	[BeginDateTime] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE [dbo].[OEE_Production] ADD  CONSTRAINT [PK_OEE_Production] PRIMARY KEY NONCLUSTERED 
(
	[ProductionId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
