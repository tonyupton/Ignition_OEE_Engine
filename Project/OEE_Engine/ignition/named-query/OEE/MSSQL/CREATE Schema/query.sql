SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[OEE_Context](
	[ContextId] [uniqueidentifier] NOT NULL,
	[BeginDateTime] [datetime] NOT NULL,
	[EndDateTime] [datetime] NULL,
	[EquipmentId] [uniqueidentifier] NULL,
	[IdealRateCount] [float] NULL,
	[IdealRateSeconds] [float] NULL,
	[LotNumber] [varchar](50) NULL,
	[Mode] [varchar](50) NULL,
	[Operator] [varchar](50) NULL,
	[Product] [varchar](50) NULL,
	[Shift] [varchar](50) NULL,
	[ShiftBeginDateTime] [datetime] NULL,
	[ShiftEndDateTime] [datetime] NULL,
	[Units] [varchar](50) NULL,
	[WorkOrder] [varchar](50) NULL,
	[WorkOrderBeginDateTime] [datetime] NULL,
 CONSTRAINT [PK_OEE_Context] PRIMARY KEY NONCLUSTERED 
(
	[ContextId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]


CREATE CLUSTERED INDEX [IX_OEE_Context_BeginDateTime] ON [dbo].[OEE_Context]
(
	[BeginDateTime] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]




CREATE TABLE [dbo].[OEE_Downtime](
	[DowntimeId] [uniqueidentifier] NOT NULL,
	[BeginDateTime] [datetime] NOT NULL,
	[EndDateTime] [datetime] NULL,
	[ContextId] [uniqueidentifier] NULL,
	[EventDateTime] [datetime] NULL,
	[Category] [varchar](50) NULL,
	[Reason] [varchar](50) NULL,
	[Planned] [bit] NULL
) ON [PRIMARY]

CREATE CLUSTERED INDEX [IX_OEE_Downtime_BeginDateTime] ON [dbo].[OEE_Downtime]
(
	[BeginDateTime] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

ALTER TABLE [dbo].[OEE_Downtime] ADD  CONSTRAINT [PK_OEE_Downtime] PRIMARY KEY NONCLUSTERED 
(
	[DowntimeId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

CREATE NONCLUSTERED INDEX [IX_OEE_Downtime_ContextId] ON [dbo].[OEE_Downtime]
(
	[ContextId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]




CREATE TABLE [dbo].[OEE_Equipment](
	[EquipmentId] [uniqueidentifier] NOT NULL,
	[Name] [varchar](50) NULL,
	[Enterprise] [varchar](50) NULL,
	[Site] [varchar](50) NULL,
	[Area] [varchar](50) NULL,
	[WorkCenter] [varchar](50) NULL,
	[WorkUnit] [varchar](50) NULL,
	[UDTPath] [varchar](255) NULL,
 CONSTRAINT [PK_OEE_Equipment] PRIMARY KEY CLUSTERED 
(
	[EquipmentId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]




CREATE TABLE [dbo].[OEE_Production](
	[ProductionId] [uniqueidentifier] NOT NULL,
	[BeginDateTime] [datetime] NOT NULL,
	[EndDateTime] [datetime] NULL,
	[ContextId] [uniqueidentifier] NULL,
	[GoodCount] [int] NULL,
	[BadCount] [int] NULL,
	[StopCount] [int] NULL,
	[DowntimeSeconds] [int] NULL,
	[RuntimeSeconds] [int] NULL,
 CONSTRAINT [PK_OEE_Production] PRIMARY KEY NONCLUSTERED 
(
	[ProductionId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]


CREATE CLUSTERED INDEX [IX_OEE_Production_BeginDateTime] ON [dbo].[OEE_Production]
(
	[BeginDateTime] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]

