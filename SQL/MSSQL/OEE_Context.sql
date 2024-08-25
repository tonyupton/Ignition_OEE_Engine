SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
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
	[WorkOrderBeginDateTime] [datetime] NULL
) ON [PRIMARY]
GO
CREATE CLUSTERED INDEX [IX_OEE_Context_BeginDateTime] ON [dbo].[OEE_Context]
(
	[BeginDateTime] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE [dbo].[OEE_Context] ADD  CONSTRAINT [PK_OEE_Context] PRIMARY KEY NONCLUSTERED 
(
	[ContextId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
